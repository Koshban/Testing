'''
You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list.
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: list1 = [], list2 = []
Output: []
Example 3:

Input: list1 = [], list2 = [0]
Output: [0]

'''
import unittest

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"ListNode({self.val})"

class Solution:
    def mergeTwoLists(self, list1, list2):
        dummy = ListNode()
        tail = dummy
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        tail.next = list1 if list1 else list2        
        return dummy.next   
    
    @staticmethod
    def list_to_linkedlist(nums: list[int]):
        dummy = ListNode()
        current = dummy
        for value in nums:
            current.next = ListNode(value)
            current = current.next
        
        return dummy.next
    
    @staticmethod
    def liinkedlist_to_list(head):
        result = []
        while head:
            result.append(head.val)
            head = head.next
        return result
                
class TestmergeTwoLists(unittest.TestCase):
    def test_mergeTwoLists(self):
        solution = Solution()
        test_data = [{'input':[[1,2,4],[1,3,4]], 'output' : [1,1,2,3,4,4]},
                    {'input':[[],[0]], 'output':[0]},
                    {'input':[[],[]], 'output':[]},
        ]
        for case in test_data:
            with self.subTest(case=case):
                l1 = solution.list_to_linkedlist(case['input'][0])
                l2 = solution.list_to_linkedlist(case['input'][1])
                mergedhead = solution.mergeTwoLists(l1, l2)
                actual = solution.liinkedlist_to_list(mergedhead)
                expected = case['output']
                self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
