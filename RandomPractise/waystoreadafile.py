#Here are various ways to read and process files in Python, from simplest to more specialized:

# 1. Basic Read Entire File:
# ```python
# Read all at once - good for small files
with open('file.txt', 'r') as file:
    content = file.read()  # entire file as string
    lines = content.splitlines()  # split into lines

# 2. Read Line by Line (Most Common):
# ```python
# Memory efficient - reads one line at a time
with open('file.txt', 'r') as file:
    for line in file:  # file object is an iterator
        line = line.strip()  # remove whitespace/newlines
        # process line

# 3. readlines() Method:
# ```python
# Reads all lines into a list
with open('file.txt', 'r') as file:
    lines = file.readlines()  # list of lines
    for line in lines:
        line = line.strip()
        # process line

# 4. Using enumerate for Line Numbers:
# ```python
with open('file.txt', 'r') as file:
    for line_num, line in enumerate(file, 1):  # start counting at 1
        print(f"Line {line_num}: {line.strip()}")

# 5. Reading Chunks:
# ```python
def read_in_chunks(file_path, chunk_size=1024):
    with open(file_path, 'r') as file:
        while chunk := file.read(chunk_size):  # walrus operator (Python 3.8+)
            yield chunk

# Usage
for chunk in read_in_chunks('large_file.txt'):
    # process chunk
    pass

# 6. Using fileinput (Multiple Files):
# ```python
import fileinput

# Read from multiple files
with fileinput.input(files=('file1.txt', 'file2.txt')) as f:
    for line in f:
        print(f"File {fileinput.filename()}, Line {fileinput.lineno()}: {line.strip()}")

# 7. CSV Files:
# ```python
import csv

# Reading CSV
with open('data.csv', 'r') as file:
    csv_reader = csv.reader(file)
    header = next(csv_reader)  # skip header row
    for row in csv_reader:
        # process row
        pass

# Reading CSV with dictionaries
with open('data.csv', 'r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        # access by column name
        print(row['column_name'])

# 8. Reading with Context and Error Handling:
# ```python
def process_file(filepath):
    try:
        with open(filepath, 'r') as file:
            for line_num, line in enumerate(file, 1):
                try:
                    # process line
                    processed = line.strip().upper()
                    yield processed
                except Exception as e:
                    print(f"Error processing line {line_num}: {e}")
    except FileNotFoundError:
        print(f"File {filepath} not found")
    except PermissionError:
        print(f"Permission denied for {filepath}")


# 10. Generator-based Reading:
# ```python
def read_file_generator(filepath):
    with open(filepath, 'r') as file:
        for line in file:
            # Pre-process line
            line = line.strip()
            if not line or line.startswith('#'):  # skip empty lines and comments
                continue
            yield line

# Usage
for line in read_file_generator('file.txt'):
    # process line
    pass

# 11. Parallel Processing for Large Files:
# ```python
from concurrent.futures import ProcessPoolExecutor
from functools import partial

def process_line(line):
    # Process single line
    return line.strip().upper()

def process_file_parallel(filepath, max_workers=4):
    with open(filepath, 'r') as file:
        with ProcessPoolExecutor(max_workers=max_workers) as executor:
            results = executor.map(process_line, file)
            return list(results)

# 12. Reading with Filtering:
# ```python
def read_filtered_lines(filepath, filter_func):
    with open(filepath, 'r') as file:
        return [line.strip() for line in file if filter_func(line)]

# Usage
numbers = read_filtered_lines('data.txt', 
                            lambda x: x.strip().isdigit())
# Choose the method based on your needs:
# - Simple line-by-line reading: Method 2
# - Small files: Method 1 or 3
# - Large files: Method 5 or 11
# - Multiple files: Method 6
# - CSV data: Method 7
# - Error handling important: Method 8
# - Memory efficiency important: Method 2 or 10

