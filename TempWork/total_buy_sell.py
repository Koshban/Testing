'''
Do an aggregation of total BUY and SELL for the day
 input: A file of the below format, where in 1st line 5 is the total number of your Executions

    5
    20220210182932, BUY, 10, IBM, 39
    20220210182932, BUY, 12, HUBS, 235.78
    20220210182932, SELL, 11, TCS, 235.78
    20220210182932, SELL, 18, DOCU, 235.78
    20220210182932, BUY, 16, SKLZ, 235.78

 Output: Print the total Buy and sell amount in format BA SA
'''
import unittest
import argparse
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def buy_sell_aggregle(filename : str):
    print(f"File is {filename}")
    with open(file=filename, mode='r', encoding='utf-8') as f_read:
        count = int(f_read.readline().strip())
        b_qty, s_qty = 0.0, 0.0
        for n in range(1, count + 1):
            data = f_read.readline().strip().split(', ')
            print(f"data is {data}")
            if 'BUY' in data:
                b_qty += float(data[2]) * float(data[4])
            elif 'SELL' in data:
                s_qty += float(data[2]) * float(data[4])
            else:
                pass
        return (b_qty, s_qty)


def get_args():
    parser = argparse.ArgumentParser(description="Total BUY SELL for the day")
    parser.add_argument("-f", "--filename", required=False, type=str, default="buysell.txt", help="Input FIlename")
    myargs = parser.parse_args()
    return myargs.filename

if __name__ == "__main__":
    filename= get_args()
    filename = f'{BASE_DIR}\\{filename}'
    print(buy_sell_aggregle(filename=filename))

