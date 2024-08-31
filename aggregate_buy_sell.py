"""
Do an aggregation of total BUY and SELL for the day
 input : A file of below format,where in 1st line 5 are the total number of your Executions

    5
    20220210182932, BUY, 10, IBM, 39
    20220210182932, BUY, 12, HUBS, 235.78
    20220210182932, SELL, 11, TCS, 235.78
    20220210182932, SELL, 18, DOCU, 235.78
    20220210182932, BUY, 16, SKLZ, 235.78

 Output : Print the total Buy and sell amount in format BA SA
"""

import argparse
import os
from collections import namedtuple
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
print(BASE_DIR)



def get_count(filename: str) ->tuple:
    filename = f'{BASE_DIR}\\{filename}'
    buy_notional, sell_notional = 0.0, 0.0
    with open(mode='r', encoding='utf-8', file=filename) as f_r:
        count = int(f_r.readline().strip())
             
        for count in range(1, count + 1):
            data = f_r.readline().strip().split(', ')
            print(f"for Count: {count}, Data is : {data}")
            if 'BUY' in data:
                buy_notional += float(data[2]) * float(data[4])
                # print(f"BUY Notional is  {buy_notional}")
            elif 'SELL' in data:
                sell_notional += float(data[2]) * float(data[4])
                # print(f"BUY Notional is  {sell_notional}")
            else:
                return 0
    return (buy_notional, sell_notional)

def get_args():
    parser = argparse.ArgumentParser(description="BUY SELL Total Counts")
    parser.add_argument('-f', '--filename', required=True, type=str, help = "input filename")
    # Example of multiple Args to be returned
    # parser.add_argument('-o', '--output', required=False, type=str, help="output filename")
    # parser.add_argument('-d', '--debug', required=False, action='store_true', help="enable debug mode")
    # parser.add_argument('-t', '--threshold', required=False, type=int, help="threshold value")
    # parser.add_argument('-l', '--log', required=False, type=str, help="log filename")
    myargs = parser.parse_args()
    
    # # Create a named tuple to store the arguments
    # Args = namedtuple('Args', ['filename', 'output', 'debug', 'threshold', 'log'])
  
    # # Return the parsed arguments as a named tuple
    # return Args(myargs.filename, myargs.output, myargs.debug, myargs.threshold, myargs.log)
    return myargs.filename

if __name__ == '__main__':
    # Usage example if multiple Args were being returned
    # args = get_args()
    # print(args.filename)
    # print(args.output)
    # print(args.debug)
    # print(args.threshold)
    # print(args.log)
    file = get_args()
    print(f'file is {file}')
    print(get_count(filename=file))
