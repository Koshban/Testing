"""
Find all files inside a folder and its subfolders of a given pattern e.g. Trade_{pattern}.csv
Where pattern is date in YYYYMMDD format

The folder structure could be like the below.
/home/kaushik/trade1
              trade2
                    trade3 --> ln-s of /home/alex/orders
Process the data in those files do a sum of the values in 2nd column , so line[1].
Data will be of below format
a,-5,-1,-1,0
a,10,-1,-1,0

Optimize your code to process thousands of big files 
"""
import argparse
import os
import csv
from datetime import datetime
from multiprocessing import Pool


def find_all_files(rootdir: str):
    for root, dirs, files in os.walk(rootdir):
        # print(f"Root : {root} Dir {dir} file {files}")
        #Ignore Hidden files and folders or venvs and Python files
        dirs[:] = [d for d in dirs if not d.startswith('.') or 'env' in d]
        files[:] = [f for f in files if not f.startswith('.') and '.csv' in f]
        # print(f"file {files}\n")
        for file in files:
            if file and file.startswith("Trade_") and file.endswith(".csv"):
                print(file)
                try:
                    #Extract the Date part anc cofnirm it matches YYYYMMDD pattern
                    date_str = file.split("_")[1].split(".")[0]
                    print(date_str)
                    # [File: Trade_20220101.csv] -> Extract date -> Valid date -> Path is yielded
                    # [File: Trade_20220132.csv] -> Extract date -> Invalid date (ValueError) -> Path is not yielded, continue
                    # [File: Trade_.csv]         -> Missing date -> Path is not yielded, continue
                    # [File: OtherFile.csv]      -> Pattern does not match -> Path is not yielded, continue
                    datetime.strptime(date_str, '%Y%m%d')
                    # Yield a file as soon as its verified, not return all of them at same time. This enables multiprocessing.
                    yield(os.path.join(root, file))
                except ValueError:
                    continue                                    

def find_sums(input: str) -> int:
    tot_sum = 0    
    with open(file=input, mode='r', encoding='utf-8') as file_read:
        csv_reader = csv.reader(file_read)
        # print(f"File is {csv_reader}")
        for line in csv_reader:
            try:
                if line and len(line) > 1:
                    print(f"Line is {line}")
                    tot_sum += int(line[1])
            except ValueError:
                continue
    return tot_sum

def main(rootdir: str):
    # Create a pool of worker processes
    # When you instantiate a Pool object, you create a pool of worker processes that can run tasks in parallel. The number of processes in the pool is 
    # determined by the processes argument to Pool(), which defaults to the number of CPU cores available on your machine if not specified.
    with Pool() as pool:
        # Use the generator to get the file paths and map the file processing function to the files
        # The pool.imap_unordered method is used for lazily iterating over the files
        # Instead of calling find_sums() directly,You should pass the function itself (without calling it) as the first argument to imap_unordered. 
        # The imap_unordered method will then call find_sums with each item from the iterator produced by find_all_files(rootdir=rootdir).
        result = pool.imap_unordered(find_sums, find_all_files(rootdir=rootdir))
        total_sum = sum(result)
        return total_sum


if __name__ == "__main__":
    # parser = argparse.ArgumentParser(description="Find all files in folder and sum their contents")
    # parser.add_argument('-r', '--rootfolder', required=True, type=str, help="Folder where to search the files")
    # args = parser.parse_args()
    # print(args.rootfolder)
    rootfolder=r"C:\Users\kaush\Desktop\Code\Testing"
    totalsum = main(rootdir=rootfolder)
    print(f"Total Sum of 2nd Column is : {totalsum}")
