'''
Given N number of sorted files containing numbers, combine them to create a new sorted file while taking care of any memory issues. 
'''
import unittest
import os
import argparse
import heapq

def get_args() -> argparse.ArgumentParser:
    parser  = argparse.ArgumentParser(description='Merge N sorted files into one sorted output file')
    parser.add_argument('--input_files', '-i', required=True, type=str, nargs='+', help='List of Input files to mergesort')
    parser.add_argument('--output_file', '-o', required=True, type=str, help='Output files to write final data to')
    return parser

def read_next_value(filename : str, line_number: int) -> tuple[int, int, str]:
    """Read specific line from file"""
    try:
        with open(file=filename, mode='r') as file_r:
            for i, line in enumerate(file_r):
                if i == line_number:
                    value = int(line.strip())
                    return (value, line_number + 1, filename)  
    except Exception as e:
        print(f"Error reading {filename}: {str(e)}")
    return (None, line_number, filename)
    

def merge_files(input_files: list[str], output_file: str) -> None:
    """
    Merge multiple sorted files using a min heap.
    Works directly with filenames instead of file handles.
    """
    try:
        # Initialize heap with first value from each file. and hence passing 0 in the first call of read_next_value.line_number
        heap = []
        for filename in input_files:
            value, next_line, filename = read_next_value(filename=filename, line_number=0)
            if value is not None:
                heapq.heappush(heap, (value, next_line, filename))

                
        
        # Process files and write to output
        with open(file=output_file, mode='w', encoding='utf-8') as file_w:
            while heap:
                value, line_number, filename = heapq.heappop(heap)
                file_w.write(f"{value}\n")

                next_value, next_line, filename = read_next_value(filename=filename, line_number=line_number)
                if next_value is not None:
                    heapq.heappush(heap, (next_value, next_line, filename))
    

    except Exception as e:
        print(f" An Error Occurred. {e}")

def main():
    parser = get_args()
    args = parser.parse_args()
    print(f"Current working directory: {os.getcwd()}")
    print(f"Input files: {args.input_files}")
    print(f"Output file: {args.output_file}")
    
    merge_files(args.input_files, args.output_file)
    print("Merge complete!")


if __name__ == "__main__":
    main()
    