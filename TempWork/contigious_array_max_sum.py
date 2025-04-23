"""
Given an array of integers, write a function to find the maximum sum of a contiguous subarray.
"""

def maximumSum(mylist :list[int]) -> int:
    sum, maxsum = 0, -float('inf')
    for index, number in enumerate(mylist):
        sum = max((sum + number), number)
        maxsum = max(sum, maxsum)
    return maxsum

if __name__ == '__main__':
    test_input = [-1, 3, 4, -2, 5, -7]
    print(maximumSum(mylist=test_input))