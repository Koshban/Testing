'''
S[4, 3, 6, 2, 8]
'''

def linear_sum(nums: list[int]) -> int:
    print(f"List is : {nums}")
    if len(nums) == 0:
        return 0
    else:
        for idx, num in enumerate(nums):
            return num + linear_sum(nums[idx:])


if __name__ == "__main__":
    print(linear_sum(nums=[4, 3, 6, 2, 8]))