'''
Write a function, zipper_lists, that takes in the head of two linked lists as arguments. The function should zipper the two lists together into single linked list by alternating nodes. If one of the linked lists is longer than the other, the resulting list should terminate with the remaining nodes. The function should return the head of the zippered linked list.

Do this in-place, by mutating the original Nodes.

You may assume that both input lists are non-empty.

a = Node("a")
b = Node("b")
c = Node("c")
a.next = b
b.next = c
# a -> b -> c

x = Node("x")
y = Node("y")
z = Node("z")
x.next = y
y.next = z
# x -> y -> z

zipper_lists(a, x)
# a -> x -> b -> y -> c -> z
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

x = Node("x")
y = Node("y")
z = Node("z")
x.next = y
y.next = z
# x -> y -> z

zipper_lists(a, x)
# a -> x -> b -> y -> c -> z -> d -> e -> f
s = Node("s")
t = Node("t")
s.next = t
# s -> t

one = Node(1)
two = Node(2)
three = Node(3)
four = Node(4)
one.next = two
two.next = three
three.next = four
# 1 -> 2 -> 3 -> 4

zipper_lists(s, one)
# s -> 1 -> t -> 2 -> 3 -> 4
'''
from TaroDSA.LinkedList.LinkedList_implementation import Node


def print_list(head):
    current = head
    while current is not None:
        print(current.val, end=" --> ")
        current = current.next
    
def zipper_lists(head1, head2):
    current1, tail = head1.next, head1
    current2 = head2
    counter = 0
    while current2 is not None and current1 is not None:
        if counter % 2 == 0:
            tail.next = current2
            current2 = current2.next        
        else:
            tail.next = current1
            current1 = current1.next
        tail = tail.next
        counter += 1
    
    if current1 is not None:
        tail.next = current1
    
    if current2 is not None:
        tail.next = current2
    
    return head1

if __name__ == "__main__":
    a = Node("a")
    b = Node("b")
    c = Node("c")
    a.next = b
    b.next = c
    # a -> b -> c

    x = Node("x")
    y = Node("y")
    z = Node("z")
    x.next = y
    y.next = z
    # x -> y -> z

    ziphead = zipper_lists(a, x)
    print(print_list(head=ziphead))
    # a -> x -> b -> y -> c -> z
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

    x = Node("x")
    y = Node("y")
    z = Node("z")
    x.next = y
    y.next = z
    # x -> y -> z

    ziphead = zipper_lists(a, x)
    print(print_list(head=ziphead))
    # a -> x -> b -> y -> c -> z -> d -> e -> f
    s = Node("s")
    t = Node("t")
    s.next = t
    # s -> t

    one = Node(1)
    two = Node(2)
    three = Node(3)
    four = Node(4)
    one.next = two
    two.next = three
    three.next = four
    # 1 -> 2 -> 3 -> 4
   
    ziphead = zipper_lists(s, one)
    print(print_list(head=ziphead))
    # s -> 1 -> t -> 2 -> 3 -> 4


