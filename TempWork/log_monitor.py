'''
If want to read 20+GB of log file from SOD and , in every 5 minutes  check if there a keyword, if found send mail in python 
'''
import logging
import os
import datetime
import time
import mmap
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import unittest
from unittest import mock
from io import BytesIO
import json
import requests

script_name = os.path.splitext(os.path.basename(__file__))[0]
BASE_DIR = os.path.abspath(__file__)
logging.basicConfig(
level=logging.INFO,
format='%(asctime)s - %(levelname)s - %(message)s',
handlers=[
    logging.FileHandler(f'{script_name}.log'),
    logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class LogMonitor:
    POSITION_FILE = f"{BASE_DIR}\last_position.json"
    def __init__(self, keywords: set, log_path: str, email_config: dict, chunk_size: int = 1024 * 1024):
        self.logpath = log_path
        self.keywords = keywords
        self.chunk_size = chunk_size
        self.last_position = self._get_last_position()
        
        self.email_config = email_config or {
            'smtp_server': 'smtp.gmail.com',
            'smtp_port': 587,
            'sender_email': 'kaushik.banerjee77@gmail.com',
            'password': 'DoDoFlying',
            'recipient': 'kaushik.banerjee77@gmail.com'
        }
    
    
    def _get_last_position(self) -> int:
        """Get initial file position."""
        """Load last position from file or start at 0."""
        if os.path.exists(self.POSITION_FILE):
            try:
                with open(self.POSITION_FILE, 'r') as f:
                    data = json.load(f)
                    pos = data.get(self.logpath, 0)
                    logger.info(f"Loaded last position {pos} for {self.logpath}")
                    return pos
            except Exception as e:
                logger.exception(f"Failed to load last position: {e}")
        # If no saved position, start from beginning
        logger.info(f"Starting from position 0 for {self.logpath}")
        return 0
    
    def _save_last_position(self):
        """Save last position to file."""
        try:
            data = {}
            if os.path.exists(self.POSITION_FILE):
                with open(self.POSITION_FILE, 'r') as f:
                    data = json.load(f)
            data[self.logpath] = self.last_position
            with open(self.POSITION_FILE, 'w') as f:
                json.dump(data, f)
            logger.debug(f"Saved last position {self.last_position} for {self.logpath}")
        except Exception as e:
            logger.exception(f"Failed to save last position: {e}")


    def send_email(self, matches: list[str]) -> None:
        """Send email notification with matches."""
        try:
            logger.info("Preparing email notification")
            
            msg = MIMEMultipart()
            msg['From'] = self.email_config['sender_email']
            msg['To'] = self.email_config['recipient']
            msg['Subject'] = f"Keywords Found in Log File - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"

            body = "The following matches were found:\n\n"
            body += "\n".join(matches[:10])
            if len(matches) > 10:
                body += f"\n\n... and {len(matches) - 10} more matches"

            msg.attach(MIMEText(body, 'plain'))

            with smtplib.SMTP(self.email_config['smtp_server'], 
                             self.email_config['smtp_port']) as server:
                server.starttls()
                server.login(
                    self.email_config['sender_email'],
                    self.email_config['password']
                )
                server.send_message(msg)
                
            logger.info("Email notification sent successfully")

        except Exception as e:
            logger.error(f"Failed to send email: {e}")

    def send_symphony_alert(self, matches: list[str]) -> None:
        """Send alert messages to Symphony chat."""
        try:
            logger.info("Preparing Symphony alert")

            # Your Symphony bot credentials and config
            symphony_config = self.email_config.get('symphony', {})
            session_token = symphony_config.get('session_token')  # Auth token
            key_manager_token = symphony_config.get('key_manager_token')  # Auth token
            pod_url = symphony_config.get('pod_url')  # e.g. https://pod.symphony.com
            agent_url = symphony_config.get('agent_url')  # e.g. https://agent.symphony.com
            stream_id = symphony_config.get('stream_id')  # Room or chat stream ID

            if not all([session_token, key_manager_token, pod_url, agent_url, stream_id]):
                logger.error("Missing Symphony configuration")
                return

            # Construct the message text (limit length if needed)
            message_text = "Keywords found in log:\n" + "\n".join(matches[:10])
            if len(matches) > 10:
                message_text += f"\n... and {len(matches) - 10} more matches"

            # Symphony message payload (using simple text format)
            data = {
                "message": f"<messageML>{message_text}</messageML>",
                "format": "MESSAGEML",
                "version": "2.0"
            }

            headers = {
                'sessionToken': session_token,
                'keyManagerToken': key_manager_token,
                'Content-Type': 'application/json'
            }

            url = f"{agent_url}/v4/stream/{stream_id}/message/create"

            response = requests.post(url, headers=headers, data=json.dumps(data))

            if response.status_code == 200:
                logger.info("Symphony alert sent successfully")
            else:
                logger.error(f"Failed to send Symphony alert: {response.status_code} {response.text}")

        except Exception as e:
            logger.error(f"Exception sending Symphony alert: {e}")

    def search_keywords(self):
        """Check for new occurrences of keywords using memory mapping."""
        matches = []
        
        try:
            logger.debug(f"Checking for keywords in {self.log_path}")
            
            
            # file.seek(0, 2) # Move Pointer to end of file
            # file_size = file.tell() # Get the size of the file (in bytes) by asking the current pointer position.
            # Doing the same in more easily readable format
            file_size = os.path.getsize(self.logpath)
            
            if file_size < self.last_position:
                logger.warning("File has been truncated, resetting position")
                self.last_position = 0
            
            if file_size <= self.last_position:
                logger.debug("No new content to process")
                return matches

                logger.debug(f"Processing from position {self.last_position}")
            with open(self.log_path, 'rb') as file:
                
                with mmap.mmap(file.fileno(), 0, access=mmap.ACCESS_READ) as mm:
                    mm.seek(self.last_position)
                    
                    chunks_processed = 0
                    while True:
                        chunk = mm.read(self.chunk_size)
                        if not chunk:
                            break
                            
                        chunks_processed += 1
                        try:
                            text = chunk.decode('utf-8')
                            
                            for line in text.splitlines():
                                if any(keyword.lower() in line.lower() 
                                      for keyword in self.keywords):
                                    matches.append(line)
                                    logger.debug(f"Match found: {line[:100]}...")
                                    
                        except UnicodeDecodeError:
                            logger.exception(f"Could not decode chunk at position {mm.tell()}")
                            continue
                    
                    self.last_position = mm.tell()
                    self._save_last_position()  # Save position after processing
                    logger.info(f"Processed {chunks_processed} chunks, found {len(matches)} matches")

        except FileNotFoundError:
            logger.exception(f"Log file not found: {self.log_path}")
        except Exception as e:
            logger.exception(f"Error reading log file: {e}")
            
        return matches

    def monitor(self, interval: int = 300):
        """Monitor log file at specified intervals."""
        logger.info(f"Starting monitoring of {self.log_path} with {len(self.keywords)} keywords")
        
        try:
            while True:
                matches = self.check_for_keywords()
                
                if matches:
                    logger.info(f"Found {len(matches)} matches")
                    self.send_email(matches)
                    self.send_symphony_alert(matches)
                else:
                    logger.debug("No matches found in this iteration")
                    
                logger.debug(f"Sleeping for {interval} seconds")
                time.sleep(interval)
                
        except KeyboardInterrupt:
            logger.info("Monitoring stopped by user")
        except Exception as e:
            logger.exception(f"Unexpected error: {e}")
            raise

def main():
    
    log_path = f"{BASE_DIR}/mylonglogs.log"
    keywords = {"error", "warning", "critical"}
    email_config = {
        'smtp_server': 'smtp.gmail.com',
        'smtp_port': 587,
        'sender_email': 'your-email@gmail.com',
        'password': 'your-app-password',
        'recipient': 'recipient@example.com'
    }
    
    try:
        monitor = LogMonitor(log_path, keywords, email_config)
        monitor.monitor(interval=300)
    except Exception as e:
        logger.error(f"Application error: {e}")
        raise

# Assuming your LogMonitor class is in log_monitor.py
# from log_monitor import LogMonitor

class TestLogMonitor(unittest.TestCase):
    def setUp(self):
        self.keywords = {"error", "warning"}
        self.log_path = "dummy.log"
        self.email_config = {
            'smtp_server': 'smtp.gmail.com',
            'smtp_port': 587,
            'sender_email': 'sender@example.com',
            'password': 'password',
            'recipient': 'recipient@example.com'
        }
        self.monitor = LogMonitor(self.keywords, self.log_path, self.email_config)

    @mock.patch('os.path.getsize')
    def test_get_initial_position_file_exists(self, mock_getsize):
        mock_getsize.return_value = 1024
        pos = self.monitor._get_initial_position()
        self.assertEqual(pos, 1024)
        mock_getsize.assert_called_with(self.log_path)

    @mock.patch('os.path.getsize', side_effect=FileNotFoundError)
    def test_get_initial_position_file_not_found(self, mock_getsize):
        pos = self.monitor._get_initial_position()
        self.assertEqual(pos, 0)

    @mock.patch('builtins.open', new_callable=mock.mock_open, read_data=b"error line\ninfo line\nwarning line\n")
    @mock.patch('os.path.getsize')
    def test_search_keywords_finds_matches(self, mock_getsize, mock_file):
        # Simulate file size larger than last_position
        mock_getsize.return_value = 30
        self.monitor.last_position = 0

        # Patch mmap to simulate reading file content
        def mmap_mock(fileno, length, access):
            # mmap object with read and seek methods
            content = b"error line\ninfo line\nwarning line\n"
            mm = BytesIO(content)
            mm.seek = lambda pos, whence=0: BytesIO.seek(mm, pos, whence)
            mm.tell = lambda: mm.seek(0, 1)
            mm.read = lambda size=-1: BytesIO.read(mm, size)
            return mm

        with mock.patch('mmap.mmap', side_effect=mmap_mock):
            matches = self.monitor.search_keywords()
            self.assertTrue(any("error" in line.lower() for line in matches))
            self.assertTrue(any("warning" in line.lower() for line in matches))
            self.assertFalse(any("info" in line.lower() for line in matches))

    @mock.patch('smtplib.SMTP')
    def test_send_email_called(self, mock_smtp):
        matches = ["Error: something bad happened", "Warning: check this out"]
        self.monitor.send_email(matches)
        mock_smtp.assert_called_with(self.email_config['smtp_server'], self.email_config['smtp_port'])
        instance = mock_smtp.return_value.__enter__.return_value
        instance.send_message.assert_called_once()

    @mock.patch('os.path.getsize')
    @mock.patch('builtins.open', new_callable=mock.mock_open)
    def test_search_keywords_file_truncation(self, mock_file, mock_getsize):
        # Simulate file size smaller than last_position (truncation)
        mock_getsize.return_value = 100
        self.monitor.last_position = 200  # last_position > file size triggers reset
        with mock.patch('mmap.mmap', return_value=BytesIO(b"new content\n")):
            matches = self.monitor.search_keywords()
            self.assertEqual(self.monitor.last_position, len(b"new content\n"))

if __name__ == '__main__':
    unittest.main()

