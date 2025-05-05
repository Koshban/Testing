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
"""
import argparse
import os
import csv
from datetime import datetime


def find_all_files(rootdir: str):
    matching_files = []
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
                    datetime.strptime(date_str, '%Y%m%d') # If the Pattern doesnt Matrch it creates a ValueError whihc is then caught in the except section below
                    matching_files.append(os.path.join(root, file))
                    print(matching_files)
                except ValueError:
                    continue
    return matching_files

def find_sums(input: list) -> int:
    tot_sum = 0
    for file in files:
        with open(file=file, mode='r', encoding='utf-8') as file_read:
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

if __name__ == "__main__":
    # parser = argparse.ArgumentParser(description="Find all files in folder and sum their contents")
    # parser.add_argument('-r', '--rootfolder', required=True, type=str, help="Folder where to search the files")
    # args = parser.parse_args()
    # print(args.rootfolder)
    rootfolder=r"C:\Users\kaush\Desktop\Code\Testing"
    files = find_all_files(rootdir=rootfolder)
    totalsum = find_sums(input=files)
    print(f"Total Sum of 2nd COlumn is : {totalsum}")
