'''- Write a Python script using psutil to monitor CPU/memory per process and alert via email if a trading process exceeds 80%.'''
import psutil
import time
import smtplib
from email.message import EmailMessage
import logging
from datetime import datetime
from collections import defaultdict

# Configure logging
logging.basicConfig(
    filename='process_monitor.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Email configuration
SMTP_SERVER =""
SMTP_PORT= 0
SENDER_EMAIL = ""
SENDER_PASSWORD = ""
DESTINATION_EMAIL = ""


# Processes to monitor (add your trading process names)
PROCESSES_TO_MONITOR = [
    "trading_process1.exe",
    "trading_process2.exe"
]

def send_alert(process_name, cpu_percent, memory_percent):
    try:
        msg = EmailMessage()
        msg.set_content(f"""
        ⚠️ High Resource Usage Alert ⚠️
        
        Process: {process_name}
        CPU Usage: {cpu_percent:.2f}%
        Memory Usage: {memory_percent:.2f}%
        Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
        """)
        
        msg['Subject'] = f'Resource Alert: {process_name}'
        msg['From'] = SENDER_EMAIL
        msg['To'] = DESTINATION_EMAIL
        
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
            server.send_message(msg)
            
        logging.info(f"Alert sent for {process_name}")
    except Exception as e:
        logging.error(f"Failed to send email alert: {str(e)}")

def monitor_processes():
    while True:
        try:
            for proc in psutil.process_iter(['name', 'cpu_percent', 'memory_percent']):
                if proc.info['name'] in PROCESSES_TO_MONITOR:
                    cpu_percent = proc.info['cpu_percent']
                    memory_percent = proc.info['memory_percent']
                    
                    # Check if either CPU or memory usage exceeds 80%
                    if cpu_percent > 80 or memory_percent > 80:
                        logging.warning(
                            f"High usage detected - Process: {proc.info['name']}, "
                            f"CPU: {cpu_percent}%, Memory: {memory_percent}%"
                        )
                        send_alert(proc.info['name'], cpu_percent, memory_percent)
                    
                    # Log regular status
                    logging.info(
                        f"Process: {proc.info['name']}, "
                        f"CPU: {cpu_percent}%, Memory: {memory_percent}%"
                    )
            
            # Sleep for 5 minutes before next check
            time.sleep(300)
            
        except Exception as e:
            logging.error(f"Error in monitoring: {str(e)}")
            time.sleep(60)  # Wait a minute before retrying


def send_alert(proc_name:str, cpu_pervent: int, memory_percent: int):
    pass


def monitor_processes():
    while True:
        try:
            for ps in psutil.process_iter([
            'name', 
            'cpu_percent', 
            'memory_percent',
            'status',
            'create_time',
            'num_threads',
            'io_counters'
        ]):
                if ps.info['name'] in PROCESSES_TO_MONITOR:
                    cpu_percent = ps.info['cpu']
                    memory_percent = ps.info['memory_percent']


                    if cpu_percent >= 70 or memory_percent >= 70:
                        logging.warning(f"High usage detected - Process: {ps.info['name']}, "
                            f"CPU: {cpu_percent}%, Memory: {memory_percent}%"
                        )
                        send_alert(proc_name=ps.info['name'],cpu_pervent=cpu_percent, memory_percent=memory_percent)
                    logging.info(f"Process: {ps.info['name']}, CPU: {cpu_percent}%, Memory: {memory_percent}%")
                    time.sleep(300)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            logging.error(f"Error in monitoring")
            time.sleep(60)


def track_process_history(process_names: list[str], duration_minutes: int =5):
    history = defaultdict(lambda : {'cpu' :[], 'memory' : []})
    end_time = time.time() + (duration_minutes * 60)

    while time.time() < end_time:
        for proc in psutil.process_iter(['name', 'pid', 'cpu_percent', 'memory_percent', 'memory_info']):
            try:
                if proc.info['name'] in PROCESSES_TO_MONITOR:
                    name = proc.info['name']
                    history[name]['cpu'].append(proc.info['cpu_percent'])
                    history[name]['memory'].append(proc.info['memory_percent'])
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                continue
        time.sleep(30)
    
    # Calculate
    for name, metrics in history.items():
        avg_cpu = sum(metrics['cpu'])/len(metrics['cpu'])
        avg_memory = sum(metrics['memory'])/len(metrics['memory'])
        max_cpu = max(metrics['cpu'])
        max_memory = max(metrics['memory'])


if __name__ == "__main__":
    logging.info("Process monitoring started")
    monitor_processes()