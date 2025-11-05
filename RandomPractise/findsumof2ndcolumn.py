"""
There are a number of CSV files scattered throughout a folder and its subfolders, containing information about trades.
Write a python script to find all of these CSV files and sum all of the values in the **second** column. The second column always contains integers.


For example, given a folder like


      .
    |-- a
    |   `-- b
    |       `-- ex.csv
    |-- example.csv
    `-- ignoreme.log
r
with


    # ex.csv:
    a,5,-1,-1,0
    a,10,-1,-1,0
   
    # example.csv
    sum = 450
    450 -3
    b,0,-1,-1,0
    b,-3,-1,-1,0


it should return `12 (5+10+0-3)`.
"""
import os
import logging


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
scriptname = os.path.splitext(os.path.basename(__file__))[0]
LOG_FORMAT = '%(asctime)s - %(levelname)s -[%(filename)s - %(funcName)s] : %(message)s'
logsdir = os.path.join(BASE_DIR,"logs")
os.makedirs(logsdir, exist_ok=True)
logpath = os.path.join(logsdir, f'{scriptname}.log')
logging.basicConfig(
    level = logging.DEBUG,
    format = LOG_FORMAT,
    handlers= [
        logging.StreamHandler(),
        logging.FileHandler(logpath)
    ]
)

logger = logging.getLogger(__name__)

def find_sums(filenames: list[str]) -> int:
    sum = 0
    if not filenames:
        logger.warning("No CSV files found")
        return sum
    
    for file in filenames:
        if not os.path.isfile(file) or os.path.getsize(file) == 0 or not os.access(file, os.R_OK):
            logger.warning(f"File : {file} doe snot exist or is not readable or is on Size ZERO. Please check")
            continue
        try:
            with open(file=file, mode='r', encoding='utf-8') as fileread:
                for line_number, line in enumerate(fileread, start=1):
                    line = line.strip()
                    if not line:
                        continue
                    logger.debug(f"LIne is : {line}")
                    if ',' in line:
                        try:
                            columns = line.split(',')
                            if len(columns) < 2:
                                logger.warning(f"Line {line_number} has insufficient columns: {line}")
                                continue
                            data = columns[1].strip()
                            logger.info(f"Data is : {data}")
                            
                            sum += int(data)
                            logger.info(f"Inside SUM is {sum}")
                        except Exception as e:
                            logger.warning(f"Encountered Error : {e}")
                            continue
                          
        except Exception as e:
            logger.exception(f"Error Encountered : {e}")
            break
    logger.info(f"SUM is {sum}")
    return sum
        
def find_files(root_dir: str, exclude_folders: list[str] = None):
    logger.info(BASE_DIR)
    logger.info(scriptname)
    if not exclude_folders:
        exclude_folders = []
    csv_files = []
    for root, dirs, files in os.walk(root_dir):
        dirs[:] = [d for d in dirs if d not in exclude_folders and not d.startswith('.')]
        logger.debug(f"Current root: {root}")
        logger.debug(f"Dirs after exclusion: {dirs}")
        logger.info(f"Files is : {files}")
        for file in files:
            if file.startswith('.'):
                logger.debug(f"Skipping hidden file: {file}")
                continue
            
            if file.endswith('.csv'):
                full_path = os.path.join(root, file)
                csv_files.append(full_path)
    
    logger.info(f"Found CSV files: {csv_files}")
    return csv_files

if __name__ == "__main__":
    excluded = ['ignorefolder', 'tmp']
    filenames = find_files(root_dir=BASE_DIR, exclude_folders=excluded)
    finalsum = find_sums(filenames=filenames)
    logger.info(f"Final Sum is : {finalsum}")