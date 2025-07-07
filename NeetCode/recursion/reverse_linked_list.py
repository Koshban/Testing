'''
Given the beginning of a singly linked list head, reverse the list, and return the new beginning of the list.

Example 1:

Input: head = [0,1,2,3]

Output: [3,2,1,0]
Example 2:

Input: head = []

Output: []
'''
from LinkedLists.implement_linked_List import ListNode

class Solution:
    # Iteratively T O(N) and M O(1)
    def reverseList(self, head: ListNode) -> ListNode:
        prev, curr = None, head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev
    
    # Recursively T O(N) and M O(N)
    def reverseList(self, head: ListNode) -> ListNode:
        
        if not head:
            return None
        
        Newhead = head
        if head.next:
            Newhead = self.reverseList(head.next)
            head.next.next = head
        head.next = None

        return Newhead

        