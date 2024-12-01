''' Implement a Linked List'''

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

a = Node('A')
b = Node('B')
c = Node('C')
d = Node('D')

a.next = b
b.next = c
c.next = d

# Iteratively
# def print_list(head):
#     current = head
#     while current is not None:
#         print(current.val, " --> ", end = " ")
#         current = current.next
        
#     if current is None:
#         print("None")

# Recursively
def print_list(head):
    current = head
    if current is None:
        print("None")
        return
    else:
        print(current.val, " --> ", end = " ")
        print_list(head=current.next)


#print_list(head=a)



