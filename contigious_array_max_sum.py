"""
Given an array of integers, write a function to find the maximum sum of a contiguous subarray.
"""

def maximumSum(mylist: list) -> int:
    sumofnums, max_sums = 0, -float('inf')
    for num in mylist:
        sumofnums = max(num, sumofnums + num)
        max_sums = max(sumofnums, max_sums)
        print(f"Num : {num} sumofnums : {sumofnums} and max_sum: {max_sums}")
    
    return max_sums




if __name__ == '__main__':
    test_input = [-1, 3, 4, -2, 5, -7]
    print(maximumSum(mylist=test_input))