import argparse
from collections import namedtuple
import heapq
import os
import numpy as np
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def sort_file_using_heapq(inputfiles: str):
    # File Pointers
    pq, filepointer = [], []
    for input_file in inputfiles:
        fp = open(file=f"{BASE_DIR}\\input_file", mode="r")
        filepointer.append(fp)
        line = fp.readline().strip()
        if line:
            heapq.heappush(pq, (int(line), fp)) # to make it largest Negate the number to simulate max-heap heapq.heappush(pq, (-int(line), fp))
    return pq, filepointer


def merge_and_write(pq, filepointer, outputfile):
    with open(file=outputfile, mode='w', encoding='utf-8') as fw:
        while pq:
            smallestnum, fp = heapq.heappop(pq)
            # For largest to smallest, Since we pushed negated numbers, pop will give us the largest number. Negete it back to 
            # Negate it back to get the original positive number
            # original_num = -negated_num
            fw.write(f"{smallestnum}\n") 
            next_line = fw.readline().strip()
            if next_line:
                heapq.heappush(pq, (int(next_line), fp))
    for fp in filepointer:
        fp.close()

def merge_sort_file_using_numpy(inputfiles: str):
    numbers = []
    for input_file in inputfiles:
        file= f'{BASE_DIR}\\input_file'
        numbers.append(np.loadtxt(file))
    combined_array = np.concatenate(numbers)
    sorted_numbers = np.sort(combined_array)
    return sorted_numbers

def write_numpy_sorted_file(sorted_numbers, output_file):
    output_file = f'{BASE_DIR}\\output_file'
    with open(file=output_file, mode='w', encoding='utf-8') as f_write:
        for number in sorted_numbers:
            f_write.write(number)


def get_args():
    parser = argparse.ArgumentParser(description="FIlein to sort")
    parser.add_argument("-i", "--input-file-list", nargs= '+', required=True, help="Input file list")
    parser.add_argument("-o", "--out-file", type=str, required=False, help="Output file Name")
    args = parser.parse_args()
    Args = namedtuple('Args', ['input_file_list', 'out_file'])
    return Args(input_file_list=args.input_file_list, out_file=args.out_file)

if __name__ == "__main__":
    args = get_args()
    print("Input file : ", args.input_file_list)
    print("OutFIle : ", args.out_file)
    pq, filepointer = sort_file_using_heapq(inputfiles=args.input_file_list)
    merge_and_write(pq=pq, filepointer=filepointer, outputfile=f'{BASE_DIR}\\args.out_file')
