'''
Design your implementation of the linked list. You can choose to use a singly or doubly linked list.
A node in a singly linked list should have two attributes: val and next. val is the value of the current node, and next is a pointer/reference to the next node.
If you want to use the doubly linked list, you will need one more attribute prev to indicate the previous node in the linked list. Assume all nodes in the linked list are 0-indexed.

Implement the MyLinkedList class:

    MyLinkedList() Initializes the MyLinkedList object.
    int get(int index) Get the value of the indexth node in the linked list. If the index is invalid, return -1.
    void addAtHead(int val) Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
    void addAtTail(int val) Append a node of value val as the last element of the linked list.
    void addAtIndex(int index, int val) Add a node of value val before the indexth node in the linked list. If index equals the length of the linked list, the node will be appended to the end of the linked list. If index is greater than the length, the node will not be inserted.
    void deleteAtIndex(int index) Delete the indexth node in the linked list, if the index is valid.

    Input
["MyLinkedList", "addAtHead", "addAtTail", "addAtIndex", "get", "deleteAtIndex", "get"]
[[], [1], [3], [1, 2], [1], [1], [1]]
Output
[null, null, null, null, 2, null, 3]

Explanation
MyLinkedList myLinkedList = new MyLinkedList();
myLinkedList.addAtHead(1);
myLinkedList.addAtTail(3);
myLinkedList.addAtIndex(1, 2);    // linked list becomes 1->2->3
myLinkedList.get(1);              // return 2
myLinkedList.deleteAtIndex(1);    // now the linked list is 1->3
myLinkedList.get(1);              // return 3

'''
import unittest

class ListNode:
    def __init__(self, val):
        self.val = val
        self.prev = self.next = None
    
    def __repr__(self):
        f"ListNode({self.val})"


class MyLinkedList:
    

    def __init__(self):
        ''' 2 Dummy Nodes with Val=0 to take care of edge cases
            None <==> O <==> O <==> None
        '''
        self.left = ListNode(0)
        self.right = ListNode(0)
        self.left.next = self.right
        self.right.prev = self.left
        

    def get(self, index: int) -> int:
        curr = self.left.next
        while curr and index > 0:
            curr = curr.next
            index -= 1
        
        if curr and curr != self.right and index == 0:
            return curr.val
        else:
            return -1        

    def addAtHead(self, val: int) -> None:
        node, next, prev = ListNode(val), self.left.next, self.left
        prev.next = node
        next.prev = node
        node.next = next
        node.prev = prev        

    def addAtTail(self, val: int) -> None:
        node, next, prev = ListNode(val), self.right, self.right.prev
        prev.next = node
        next.prev = node
        node.next = next
        node.prev = prev
        

    def addAtIndex(self, index: int, val: int) -> None:
        curr = self.left.next
        while curr and index > 0:
            curr = curr.next
            index -= 1
        if curr and index == 0:
            node, next, prev = ListNode(val), curr, curr.prev
            prev.next = node
            next.prev = node
            node.next = next
            node.prev = prev        

    def deleteAtIndex(self, index: int) -> None:
        curr = self.left.next
        while curr and index > 0:
            curr = curr.next
            index -= 1
        if curr and index == 0 and curr != self.right:
            next, prev = curr.next, curr.prev
            prev.next = next
            next.prev = prev

class TestMyLinkedList(unittest.TestCase):
    def test_linked_list_operations(self):
        test_cases = [
            {
                'operations': ['MyLinkedList', 'addAtHead', 'addAtTail', 'addAtIndex', 'get', 'deleteAtIndex', 'get'],
                'inputs': [[], [1], [3], [1, 2], [1], [1], [1]],
                'outputs': [None, None, None, None, 2, None, 3]
            },
            {
                'operations': ['MyLinkedList', 'addAtHead', 'addAtHead', 'addAtHead', 'addAtIndex', 'deleteAtIndex', 'addAtHead', 'addAtTail', 'get', 'addAtHead', 'addAtIndex', 'addAtHead'],
                'inputs': [[], [1], [2], [3], [1,4], [1], [6], [4], [4], [4], [5,0], [6]],
                'outputs': [None, None, None, None, None, None, None, None, 4, None, None, None]
            },
            {
                'operations': ['MyLinkedList', 'addAtHead', 'get', 'addAtHead', 'addAtHead', 'deleteAtIndex', 'addAtHead', 'get', 'get', 'get'],
                'inputs': [[], [4], [1], [1], [5], [3], [7], [3], [3], [3]],
                'outputs': [None, None, -1, None, None, None, None, 4, 4, 4]
            }
        ]
        
        for case in test_cases:
            with self.subTest(case=case):
                linked_list = None
                for i in range(len(case['operations'])):
                    operation = case['operations'][i]
                    input_val = case['inputs'][i]
                    expected_output = case['outputs'][i]
                    
                    if operation == 'MyLinkedList':
                        linked_list = MyLinkedList()
                        actual_output = None
                    elif operation == 'get':
                        actual_output = linked_list.get(input_val[0])
                    elif operation == 'addAtHead':
                        actual_output = linked_list.addAtHead(input_val[0])
                    elif operation == 'addAtTail':
                        actual_output = linked_list.addAtTail(input_val[0])
                    elif operation == 'addAtIndex':
                        actual_output = linked_list.addAtIndex(input_val[0], input_val[1])
                    elif operation == 'deleteAtIndex':
                        actual_output = linked_list.deleteAtIndex(input_val[0])
                    
                    self.assertEqual(actual_output, expected_output)

if __name__ == '__main__':
    unittest.main()
     
        