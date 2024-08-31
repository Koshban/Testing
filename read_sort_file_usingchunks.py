''' 
Files passed by arguments
Each file has only integers, assume file is already sorted
Big Files
create one output file with all the numbers in it in a sorted manner
Ensure it is efficient program
'''
import argparse
import heapq
from typing import List, Iterator
import os
import time, psutil

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
print(BASE_DIR)

def get_file_sizes(filename: str) -> int:
    return os.path.getsize(filename=filename) / (1024 * 1024) # In MB 

def file_iterator(filename: str) -> Iterator[int]:
    i = 0
    ''' Read from file at a time in chunks'''
    with open(file=f'{BASE_DIR}\\{filename}', mode='r', encoding='utf-8') as file_r:
        for line in file_r:
            yield int(line)

def read_in_chunks(filenames: list[str]) -> Iterator[int]:
    """Read integers from multiple files in chunks."""
    file_iterators = [file_iterator(filename=filename) for filename in filenames]
    return heapq.merge(*file_iterators)

def write_to_file(iterator: Iterator[int], outputfile: str, buffersize: int = 1000000):
    """Write sorted integers to the output file."""
    buffer = []
    with open(file=f'{BASE_DIR}\\{outputfile}', mode='w', encoding='utf-8') as file_w:
        for num in iterator:
            buffer.append(str(num))
            if len(buffer) >= buffersize:
                #print(f"Buffer is {buffer}")
                file_w.write('\n'.join(buffer) + '\n')
                buffer.clear()
        if buffer:
            file_w.write('\n'.join(buffer) + '\n')

def get_memory_usage():
    process = psutil.Process(os.getpid())
    return process.memory_info().rss // ( 1024 * 1024)  # In MBs

def get_args():
    parser = argparse.ArgumentParser(description="Raed and sort int files. Pass in the filenames")
    parser.add_argument("-f", "--inputfiles", type=str, required=True, nargs='+', help="Input comma separated file names.")
    parser.add_argument("-o", "--outputfile", required=False, default="Output.txt", help="name of output file.")
    parser.add_argument('-c', '--chunksize', default = 32 * 1024 * 1024, required=False, help='Number of lines to read at a time ')
    args = parser.parse_args()
    return args

if __name__ == "__main__":
    total_input_size = 0
    start_time = time.time()
    args = get_args()
    filenames, outputfile, chunksize = args.inputfiles, args.outputfile, args.chunksize
    print("*" * 20 , "Input File Size.", "*" * 20, "\n")
    for filename in filenames:
        size = get_file_sizes(filename=filename)
        print(f"FileSize of {filename} is : {size:.3f} MBs")
        total_input_size += size
    
    print(f"\nStarting sort operation...")
    sort_start_time = time.time()
    sorted_iterator = read_in_chunks(filenames=filenames)
    sort_memory = get_memory_usage()
    print(f"Memory usage after creating Iterator : {sort_memory:.3f} MBs.")

    write_start_time = time.time()
    write_to_file(iterator=sorted_iterator, outputfile=outputfile)
    write_memory = get_memory_usage()
    print(f"Memory usage after creating Writing : {write_memory:.3f} MBs.")

    output_size = get_file_sizes(outputfile)
    print(f"\nOutput file size: {output_size:.3f} MBs")
    end_time = time.time()
    
    print(f"\nTime spent:")
    print(f"Total time: {end_time - start_time:.2f} seconds")
    print(f"Sort preparation time: {write_start_time - sort_start_time:.2f} seconds")
    print(f"Write time: {end_time - write_start_time:.2f} seconds")
    
    print(f"\nMax memory usage: {max(sort_memory, write_memory):.2f} MBs")

    print(f"Sorting complete. Results written to {outputfile}")



