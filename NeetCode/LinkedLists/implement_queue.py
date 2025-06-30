'''
Implement a Queue using LinkedLists
'''
from implement_linked_List import ListNode

class Queue:
    def enque(self, val):
        newNode = ListNode(val=val)

        if self.right:
            self.right.next = newNode
            self.right = self.right.next
        else:
            self.left = self.right = newNode
    
    def deque(self):
        if not self.left:
            return None
        
        val = self.left.val
        self.left = self.left.next
        if not self.left:
            self.right = None
        return val