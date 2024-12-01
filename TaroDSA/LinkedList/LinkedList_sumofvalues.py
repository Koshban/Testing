'''
Write a function, sum_list, that takes in the head of a linked list containing numbers as an argument. The function should return the total sum of all values in the linked list.

a = Node(2)
b = Node(8)
c = Node(3)
d = Node(-1)
e = Node(7)
a.next = b
b.next = c
c.next = d
d.next = e

# 2 -> 8 -> 3 -> -1 -> 7
sum_list(a) # 19
x = Node(38)
y = Node(4)
x.next = y

# 38 -> 4
sum_list(x) # 42
'''

from TaroDSA.LinkedList.LinkedList_implementation import Node

# def sum_list(head) -> int:
#     sum, current = 0, head
#     try:
#         while current is not None:
#             sum += int(current.val)
#             current = current.next
#         return sum
#     except Exception as e:
#         return e

def sum_list(head) -> int:
    try:
        if head is None:
            return 0
        return head.val + sum_list(head=head.next)     
    except Exception as e:
        return e


if __name__ == "__main__":
    a = Node(2)
    b = Node(8)
    #c = Node('x')
    c = Node(3)
    d = Node(-1)
    e = Node(7)
    a.next = b
    b.next = c
    c.next = d
    d.next = e

    # 2 -> 8 -> 3 -> -1 -> 7
    print(sum_list(a)) # 19
    x = Node(38)
    y = Node(4)
    x.next = y

    # 38 -> 4
    print(sum_list(x)) # 42
