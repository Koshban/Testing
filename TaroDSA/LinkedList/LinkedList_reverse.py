'''
Write a function, reverse_list, that takes in the head of a linked list as an argument. The function should reverse the order of the nodes in the linked list in-place and return the new head of the reversed linked list.

a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")
a.next = b
b.next = c
c.next = d
d.next = e
e.next = f

# a -> b -> c -> d -> e -> f
reverse_list(a) # f -> e -> d -> c -> b -> a
x = Node("x")
y = Node("y")
x.next = y

# x -> y
reverse_list(x) # y -> x
p = Node("p")

# p
reverse_list(p) # p
'''
from TaroDSA.LinkedList.LinkedList_implementation import Node
def reverse_list(head):
    if head is None:
        return None
    return reverse_list(head = head.next)
    print(head)

def reverse_list(head):
    current, prev = head, None
    '''
    None ->     a ->        b ->        c ->        d ->        e ->    f
    Prev        Current     Next 
                Prev        Current     Next
                            Prev        Current     Next
                                        Prev        Current     Next
    '''
    while current is not None:
        next = current.next
        current.next = prev
        prev = current
        current = next
    return prev.val # As it is the new current/head

if __name__ == "__main__":
    a = Node("a")
    b = Node("b")
    c = Node("c")
    d = Node("d")
    e = Node("e")
    f = Node("f")
    a.next = b
    b.next = c
    c.next = d
    d.next = e
    e.next = f
    # a -> b -> c -> d -> e -> f
    print(reverse_list(a)) # f -> e -> d -> c -> b -> a

    x = Node("x")
    y = Node("y")
    x.next = y
    # x -> y
    print(reverse_list(x)) # y -> x

    p = Node("p")
    # p
    print(reverse_list(p)) # p
