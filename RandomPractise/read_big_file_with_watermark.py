'''If want to read 20+GB of log file from SOD and , in every 5 minutes  check if there a keyword, if found send mail in python '''
import os
import time
import re

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def read_log_file(file_path: str, last_position: int = 0, chunk_size: int= 1024*1024):
    with open(file=file_path, mode='r', encoding='utf-8') as f:
        f.seek(last_position)
        chunk = f.read(chunk_size)
        new_position = f.tell()
    return chunk, new_position

def find_pattern(file: str, pattern: str, last_position: int):
    chunk, new_position = read_log_file(file_path=file, last_position=last_position)
    match = re.search(f'.*{re.escape(pattern)}.*', chunk, re.MULTILINE)
    if match:
        return True, new_position, match.group(0)
    else:
        False, new_position, None
    
def main():
    logpath = BASE_DIR
    pattern_to_search = 'koshban'
    check_interval = 30 # 5 mins, 300 seconds
    last_position = 0

    while True:
        found, new_position, line = find_pattern(file=f'{logpath}\\logs\\large_test_file.txt', pattern=pattern_to_search, last_position=last_position)
        if found:
            print(f"Keyword '{pattern_to_search}' found in log file at {time.ctime()}")
            print(f"Matching line : {line}")
        else:
            print(f"Keyword '{pattern_to_search}' not found at {time.ctime()}")
        
        last_position = new_position
        time.sleep(check_interval)

if __name__ == "__main__":
    main()




