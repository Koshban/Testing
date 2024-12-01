'''
Write a function, linked_list_find, that takes in the head of a linked list and a target value. The function should return a boolean indicating whether or not the linked list contains the target.

a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
a.next = b
b.next = c
c.next = d

# a -> b -> c -> d
linked_list_find(a, "c") # True
a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
a.next = b
b.next = c
c.next = d

# a -> b -> c -> d
linked_list_find(a, "d") # True
a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
a.next = b
b.next = c
c.next = d

# a -> b -> c -> d
linked_list_find(a, "q") # False
'''
from TaroDSA.LinkedList.LinkedList_implementation import Node
# def linked_list_find(head, target: str) -> bool:
#     current = head
#     while current is not None:
#         if current.val == target:
#             return True
#         current = current.next
#     return False

def linked_list_find(head, target: str) -> bool:
    
    if head is None:
        return False
    if head.val == target:
        return True
    return linked_list_find(head=head.next, target=target)


if __name__ == '__main__':
    a = Node("a")
    b = Node("b")
    c = Node("c")
    d = Node("d")
    a.next = b
    b.next = c
    c.next = d

    # a -> b -> c -> d
    print(linked_list_find(a, "c")) # True
    a = Node("a")
    b = Node("b")
    c = Node("c")
    d = Node("d")
    a.next = b
    b.next = c
    c.next = d

    # a -> b -> c -> d
    print(linked_list_find(a, "d")) # True
    a = Node("a")
    b = Node("b")
    c = Node("c")
    d = Node("d")
    a.next = b
    b.next = c
    c.next = d

    # a -> b -> c -> d
    print(linked_list_find(a, "q")) # False
