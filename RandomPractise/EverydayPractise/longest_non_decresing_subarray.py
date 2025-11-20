''' Implement a function to find the longest non-decreasing subarray from two arrays.
You are given two integer arrays, A and B, each of length n.You must construct a new array C of length n, where for each i (0 ≤ i < n), you may choose either A[i] or 
B[i] as C[i]. Your task is to determine the length of the longest contiguous non-decreasing subarray that can be formed in C.
Return this maximum possible length
Input:
A = [2, 3, 1]
B = [1, 2, 1]

Output:
2
Input:
A = [8, 6, 7, 3, 4]
B = [5, 4, 3, 2, 1]

Output:
2
'''
import unittest

def longest_non_decreasing_subarray(A: list[int], B: list[int]) -> int:
    if (len(A) != len(B)) or (not A) or (not B):
        print("HERE")
        return -1
    count1, maxc1, count2, maxc2, longest = 1, 1, 1, 1, 1
    for idx in range(1, len(A)  ):
        if A[idx -1] <= A[idx]:
            count1 += 1
            maxc1 = max(maxc1, count1)
        else:
            count1 = 1
            
        if B[idx -1] <= B[idx]:
            count2 += 1
            maxc2 = max(maxc2, count2)
        else:
            count2 = 1
        longest = max(maxc1, maxc2)
        print(f"At IDX: {idx}. Arrays so far: {A[:idx]} and {B[:idx]}")
        print(f"COunts are, C1: {count1} C2: {count2} and Max1: {maxc1} and max2: {maxc2} and longest: {longest}")
    
    return longest
# A = [8, 6, 7, 3, 4]
# B = [5, 4, 3, 2, 1]
def longest_non_decreasing_across_arrays(A: list[int], B: list[int]) -> int:
    if (len(A) != len(B)) or (not A) or (not B):
        print("HERE")
        return -1
    count1, maxc1, count2, maxc2, longest, nums = 1, 1, 1, 1, 1, []
    if A[0] <= B[0]:
        nums.append(A[0])
    else:
        nums.append(B[0])
    print(f"After Step # 1 Nums is now : {nums}")
    for idx in range(1, len(A)):
        print(f"NUmber is : A : {A[idx]} and B : {B[idx]}")
        minnum = min(A[idx], B[idx])
        maxnum = max(A[idx], B[idx])
        print(f"Min is {minnum} and Max is {maxnum}")
        if nums[-1]:
            if minnum >= nums[-1]:            
                nums.append(minnum)
            elif maxnum >= nums[-1]:
                nums.append(maxnum)
            else:
                nums = []
                nums.append(minnum)
        else:
            nums.append(minnum)
            print(f"Nums is now : {nums}")

        print(f"Nums is now : {nums}")
        count1 = len(nums)
        longest = max(count1, longest)
    return longest


# Proper implementation where u create a C[i] choosing elements of A or B. Uses DP
def longest_non_decreasing_subarray(A: list[int], B: list[int]) -> int:
    if len(A) != len(B) or not A:
        return -1

    n = len(A)
    lenA = [1] * n
    lenB = [1] * n
    ans = 1

    for i in range(1, n):
        # Choose A[i]
        if A[i] >= A[i - 1]:
            lenA[i] = max(lenA[i], lenA[i - 1] + 1)
        if A[i] >= B[i - 1]:
            lenA[i] = max(lenA[i], lenB[i - 1] + 1)

        # Choose B[i]
        if B[i] >= A[i - 1]:
            lenB[i] = max(lenB[i], lenA[i - 1] + 1)
        if B[i] >= B[i - 1]:
            lenB[i] = max(lenB[i], lenB[i - 1] + 1)

        ans = max(ans, lenA[i], lenB[i])

    return ans

class TestLongestNonDecreasingSubarray(unittest.TestCase):
    # def test_case_1(self):
    #     A = [2, 3, 1]
    #     B = [1, 2, 1]
    #     self.assertEqual(longest_non_decreasing_subarray(A, B), 2)

    def test_case_2(self):
        A = [8, 6, 7, 3, 4]
        B = [5, 4, 3, 2, 1]
        self.assertEqual(longest_non_decreasing_across_arrays(A, B), 3)

    # def test_case_3(self):
    #     A = [1, 2, 3]
    #     B = [1, 2, 3]
    #     self.assertEqual(longest_non_decreasing_subarray(A, B), 3)

    # def test_case_4(self):
    #     A = [5, 4, 3]
    #     B = [3, 4, 5]
    #     self.assertEqual(longest_non_decreasing_subarray(A, B), 3)

    # def test_case_5(self):
    #     A = [1, 5, 2, 6, 3]
    #     B = [2, 1, 3, 5, 4]
    #     self.assertEqual(longest_non_decreasing_subarray(A, B), 3)

    # def test_case_6(self):
    #     A = [1, 1, 1, 1]
    #     B = [1, 1, 1, 1]
    #     self.assertEqual(longest_non_decreasing_subarray(A, B), 4)

    # def test_case_7(self):
    #     A = [1, 10, 5, 7, 9]
    #     B = [2, 3, 4, 8, 10]
    #     self.assertEqual(longest_non_decreasing_subarray(A, B), 5)

    # def test_case_8(self):
    #     A = [100]
    #     B = [200]
    #     self.assertEqual(longest_non_decreasing_subarray(A, B), 1)
    
    # def test_case_9(self):
    #     A = []
    #     B = []
    #     self.assertEqual(longest_non_decreasing_subarray(A, B), -1)
    
    # def test_case_10(self):
    #     A = [5]
    #     B = []
    #     self.assertEqual(longest_non_decreasing_subarray(A, B), -1)

if __name__ == "__main__":
    unittest.main()
