'''
Given the head of a singly linked list, reverse the list, and return the reversed list.
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
Input: head = [1,2]
Output: [2,1]
Input: head = []
Output: []
'''
import unittest
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __repr__(self):
         # Create a more informative representation of the full list
        return f"ListNode({self.val})"
    
    def debug_str(self):
        # Show the full list representation starting from this node
        nodes = []
        current = self
        while current:
            nodes.append(str(current.val))
            current = current.next
        return " -> ".join(nodes)
    
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev, curr = None, head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev
    
    def list_to_linknodes(self, nums: list):
        dummy = ListNode()
        current = dummy
        for num in nums:
            current.next = ListNode(num)
            current = current.next
        return dummy.next
    
    def linkedlist_to_list(self, head):
        nums = []
        while head:
            nums.append(head.val)
            head = head.next
        return nums
            

class TestreverseList(unittest.TestCase):
    def test_reverseList(self):
        solution = Solution()
        test_data = [{'input':[1,2,3,4,5], 'output' : [5,4,3,2,1]},
                    {'input':[1,2, 5], 'output':[5, 2,1]},
                    {'input':[], 'output':[]},
        ]
        for case in test_data:
            #print(case)
            with self.subTest(test_case=case):
                #print(case["input"])
                head = solution.list_to_linknodes(case["input"])
                reversed_head = solution.reverseList(head)
                if head:
                    print(f"Full Linked List is  is : ", head.debug_str())
                    print(f"Reversed Head is :", reversed_head.debug_str())
                actual = solution.linkedlist_to_list(reversed_head)
                expected = case['output']
                self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()