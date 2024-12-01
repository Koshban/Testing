'''
Write a function, linked_list_values, that takes in the head of a linked list as an argument. The function should return a list containing all values of the nodes in the linked list.
a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
a.next = b
b.next = c
c.next = d

# a -> b -> c -> d

linked_list_values(a) # -> [ 'a', 'b', 'c', 'd' ]
x = Node("x")
y = Node("y")
x.next = y

# x -> y

linked_list_values(x) # -> [ 'x', 'y' ]
'''

from TaroDSA.LinkedList.LinkedList_implementation import Node #, print_list as printlist

def linked_list_values(head) -> list[str]:
    values_array = []
    current = head
    while current is not None:
        values_array.append(current.val)
        current = current.next
    return values_array

if __name__ == "__main__":
    a = Node("a")
    b = Node("b")
    c = Node("c")
    d = Node("d")
    a.next = b
    b.next = c
    c.next = d

    # a -> b -> c -> d

    print(linked_list_values(a)) # -> [ 'a', 'b', 'c', 'd' ]
    x = Node("x")
    y = Node("y")
    x.next = y

    # x -> y

    print(linked_list_values(x)) # -> [ 'x', 'y' ]


    

