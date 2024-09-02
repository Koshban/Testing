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
import numpy as np
import tempfile

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
print(BASE_DIR)

def get_file_sizes(filename: str) -> int:
    return os.path.getsize(filename=filename) / (1024 * 1024) # In MB 

def get_memory_usage():
    process = psutil.Process(os.getpid())
    return process.memory_info().rss // ( 1024 * 1024)  # In MBs

def get_args():
    parser = argparse.ArgumentParser(description="Raed and sort int files. Pass in the filenames")
    parser.add_argument("-f", "--inputfiles", type=str, required=True, nargs='+', help="Input comma separated file names.")
    parser.add_argument("-o", "--outputfile", required=False, default="Output.txt", help="name of output file.")
    parser.add_argument("-o2", "--outputfile2", required=False, default="OutputKosh.txt", help="name of output file for external Merge Sort.")
    parser.add_argument('-c', '--chunksize', default = 32 * 1024 * 1024, required=False, help='Chunk size to read at a time ')
    parser.add_argument('-l', '--lines', default = 1000000, required=False, help='Number of lines to read at a time ')
    args = parser.parse_args()
    return args

''' Uisng NumPy'''
def read_and_sort_using_numpy(filenames: list[str], outputfile: str):
    data = np.concatenate([np.loadtxt(f, dtype=np.int64) for f in filenames])

    data.sort()

    np.savetxt(outputfile, data, fmt='%d')

''' Using HeapQ'''
def file_iterator_using_heapq(filename: str) -> Iterator[int]:
    i = 0
    ''' Read from file at a time in chunks'''
    with open(file=f'{BASE_DIR}\\{filename}', mode='r', encoding='utf-8') as file_r:
        for line in file_r:
            yield int(line)

def read_in_chunks_using_heapq(filenames: list[str]) -> Iterator[int]:
    """Read integers from multiple files in chunks."""
    file_iterators = [file_iterator_using_heapq(filename=filename) for filename in filenames]
    return heapq.merge(*file_iterators)

def write_to_file_using_heapq(iterator: Iterator[int], outputfile: str, buffersize: int = 1000000):
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

''' Using External Merge Sort'''
def read_and_sort_using_external_merge_sort(filenames: list[str], outputfile: str, lines_per_read: int): 
    temp_files = []
    # Phase 1 : Create Sorted Chunks
    for input_file in filenames:
        with open(file=input_file, mode='r', encoding='utf-8') as f_read:
            while True:
                chunk = []
                for _ in range(lines_per_read):
                    line = f_read.readline()
                    if not line:
                        break
                    chunk.append(int(line.strip()))
                #print(f"Chunk is {chunk}")
                if not chunk:
                    break
                chunk.sort()
                temp_file = tempfile.NamedTemporaryFile(mode='w+', delete=False)
                for num in chunk:
                    temp_file.write(f"{num}\n")
                temp_file.close()
                temp_files.append(temp_file.name)

    # Phase 2: Merge the sorted chunks
    with open(file=outputfile2, mode='w', encoding='utf-8') as file_write:
        try:
            heap = []
            files = [open(f) for f in temp_files]
            for i , f in enumerate(files):
                line = f.readline()
                if line:
                    heap.append((int(line.strip()), i))
            heapq.heapify(heap)

            while heap:
                val, i = heapq.heappop(heap)
                file_write.write(f"{val}\n")
                line = files[i]. readline()
                if line:
                    heapq.heappush(heap, (int(line.strip()), i))
        finally:
            pass
   
    
if __name__ == "__main__":
    total_input_size = 0
    start_time = time.time()
    args = get_args()
    filenames, outputfile, outputfile2, chunksize, numoflines = args.inputfiles, args.outputfile, args.outputfile2, args.chunksize, args.lines
    print("*" * 20 , "Input File Size.", "*" * 20, "\n")
    for filename in filenames:
        size = get_file_sizes(filename=filename)
        print(f"FileSize of {filename} is : {size:.3f} MBs")
        total_input_size += size
    
    print(f"\nStarting sort operation...")
    sort_start_time = time.time()
    sorted_iterator = read_in_chunks_using_heapq(filenames=filenames)
    sort_memory = get_memory_usage()
    print(f"Memory usage after creating Iterator : {sort_memory:.3f} MBs.")

    write_start_time = time.time()
    write_to_file_using_heapq(iterator=sorted_iterator, outputfile=outputfile)
    write_memory = get_memory_usage()
    print(f"Memory usage after creating Writing : {write_memory:.3f} MBs.")

    output_size = get_file_sizes(outputfile)
    print(f"\nOutput file size: {output_size:.3f} MBs")
    end_time = time.time()
    ''' HeapQ Stats'''
    print(f"\nTime spent Using HeapQ:")
    print(f"Total time: {end_time - start_time:.2f} seconds")
    print(f"Sort preparation time: {write_start_time - sort_start_time:.2f} seconds")
    print(f"Write time: {end_time - write_start_time:.2f} seconds")
    print(f"Max memory usage: {max(sort_memory, write_memory):.2f} MBs")

    '''Using Numpy'''
    numpy_start_time = time.time()
    read_and_sort_using_numpy(filenames=filenames, outputfile=outputfile)
    sort_memory_numpy = get_memory_usage()    
    numpy_end_time = time.time()

    '''Numpy Stats'''
    print(f"\nTime spent Using NumPy:")
    print(f"Total time: {numpy_end_time - numpy_start_time:.2f} seconds")
    print(f"Memory usage after Numpy : {sort_memory_numpy:.3f} MBs.")

    ''' Using External Merge Sort'''
    extmerge_start_time = time.time()
    read_and_sort_using_external_merge_sort(filenames=filenames, outputfile=outputfile2, lines_per_read=numoflines)
    sort_memory_extmerge = get_memory_usage()    
    extmerge_end_time = time.time()

    '''External Merge Stats'''
    print(f"\nTime spent Using External Merge:")
    print(f"Total time: {extmerge_end_time - extmerge_start_time:.2f} seconds")
    print(f"Memory usage after Numpy : {sort_memory_extmerge:.3f} MBs.")
    


    print(f"Sorting complete. Results written to {outputfile}")



