'''
Write a function, get_node_value, that takes in the head of a linked list and an index. The function should return the value of the linked list at the specified index.
If there is no node at the given index, then return None.

a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
a.next = b
b.next = c
c.next = d

# a -> b -> c -> d
get_node_value(a, 2) # 'c'
a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
a.next = b
b.next = c
c.next = d

# a -> b -> c -> d
get_node_value(a, 3) # 'd'
a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
a.next = b
b.next = c
c.next = d

# a -> b -> c -> d
get_node_value(a, 7) # None
'''
from TaroDSA.LinkedList.LinkedList_implementation import Node

# def get_node_value(head, index: int) -> str:
#     current, tempidx = head, 0
#     while current is not None:
#         if tempidx == index:
#             return current.val
#         current = current.next
#         tempidx += 1
#     return None

def get_node_value(head, index: int) -> str:
    if head is None:
        return None
    if index == 0:
        return head.val
    return get_node_value(head=head.next, index=index -1)
    
    

if __name__ == "__main__":
    a = Node("a")
    b = Node("b")
    c = Node("c")
    d = Node("d")
    a.next = b
    b.next = c
    c.next = d

    # a -> b -> c -> d
    print(get_node_value(a, 2)) # 'c'
    a = Node("a")
    b = Node("b")
    c = Node("c")
    d = Node("d")
    a.next = b
    b.next = c
    c.next = d

    # a -> b -> c -> d
    print(get_node_value(a, 3)) # 'd'
    a = Node("a")
    b = Node("b")
    c = Node("c")
    d = Node("d")
    a.next = b
    b.next = c
    c.next = d

    # a -> b -> c -> d
    print(get_node_value(a, 7)) # None
