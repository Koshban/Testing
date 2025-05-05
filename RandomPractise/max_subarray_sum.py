
''' Max sum of contigious elements in a SubArray
e.g. for [-1, 3, 4, -2, 5, -7] , it should be 10
'''
# def maximumSum(mylist: list) -> int:
#     sumofnums = 0
#     max_sum = -float('inf')
#     for num in mylist:
#         sumofnums = max(num, sumofnums + num)
#         max_sum = max(max_sum, sumofnums)
#         print(f"Num : {num} sumofnums : {sumofnums} and max_sum: {max_sum}")

#     return int(max_sum)




def maxsumofnums_contigious(nums: list[int]) -> int:
    if not nums:
        return -1
    sumofnums = maxsumofnums = nums[0] 
    for i, num in enumerate(nums):
        sumofnums = max(num, sumofnums + num)
        maxsumofnums = max(maxsumofnums, sumofnums)
        print(f"for Index {i}. Sum of nums is {sumofnums} and Max so far is {maxsumofnums}")
    return maxsumofnums

def maxsumofnums_noncontigious(nums: list[int]) -> int:
    if not nums:
        return -1
    sumofnums = maxsumofnums = 0 
    for i, num in enumerate(nums):
        sumofnums = max(sumofnums, sumofnums + num)
        maxsumofnums = max(maxsumofnums, sumofnums)
        print(f"for Index {i}. Sum of nums is {sumofnums} and Max so far is {maxsumofnums}")
    return maxsumofnums


if __name__ == '__main__':
    test_input = [-1, 3, 4, -2, 5, -7]
    print(maxsumofnums_contigious(nums=test_input))
    print(maxsumofnums_noncontigious(nums=test_input))


