'''
Suppose we are given three sequences of numbers, A, B, and C. We will assume that no individual sequence contains duplicate values, but that there may be some numbers that are in
two or three of the sequences. The three-way set disjointness problem is to determine if the intersection of the three sequences is empty, namely, that there is no element x such that 
x is in A, B, and C.

'''
from typing import TypeVar, Sequence,List
from typeguard import typechecked

T = TypeVar('T')

@typechecked
def is_three_way_disjoint(nums1: List[int],nums2: List[int],nums3: List[int]) -> bool:

#def is_three_way_disjoint(nums1: Sequence[int], nums2: Sequence[int],nums3: Sequence[int]) -> bool:
    #return not (set(nums1) & set(nums2) & set(nums3))  # Using SET Operations

    if not nums1 or not nums2 or not nums3:
        return True

    x, y, z = sorted((nums1,nums2, nums3),key=len)
    set_y = set(y)
    set_z = set(z)
    for element in x:
        if element in set_y and element in set_z:
            return False
    return True
# Example
if __name__ == "__main__":
    A = [1, 5, 8, 'MN']
    B = [2, 5, 9, 10]
    C = [3, 5, 7, 10]

    print(is_three_way_disjoint(A, B, C))  # False, since 5 and 10 are in all three

    D = [1,2,3]
    E = [4,5,6]
    F = [7,8,9]
    print(is_three_way_disjoint(D, E, F))  # True, no common element