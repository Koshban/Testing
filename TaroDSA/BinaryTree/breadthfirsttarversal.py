# Write a function, breadth_first_values, that takes in the root of a binary tree. The function should return a list containing all values of the tree in breadth-first 
# order.

# a = Node('a')
# b = Node('b')
# c = Node('c')
# d = Node('d')
# e = Node('e')
# f = Node('f')
# a.left = b
# a.right = c
# b.left = d
# b.right = e
# c.right = f

# #      a
# #    /   \
# #   b     c
# #  / \     \
# # d   e     f

# breadth_first_values(a)
# #    -> ['a', 'b', 'c', 'd', 'e', 'f']
# a = Node('a')
# b = Node('b')
# c = Node('c')
# d = Node('d')
# e = Node('e')
# f = Node('f')
# g = Node('g')
# h = Node('h')
# a.left = b
# a.right = c
# b.left = d
# b.right = e
# c.right = f
# e.left = g
# f.right = h

# #      a
# #    /   \
# #   b     c
# #  / \     \
# # d   e     f
# #    /       \
# #   g         h

# breadth_first_values(a)
# #   -> ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
# a = Node('a')
# #      a

# breadth_first_values(a)
# #    -> ['a']

from BinaryTreeClass import Node
from collections import deque

# Iterrative solution
def breadth_first_values(root):
    values = []
    if root is None:
        return values    
    process_queue = deque([root])
    while process_queue:        
        current = process_queue.popleft()
        values.append(current.val)
        
        if current.left is not None:
            process_queue.append(current.left)
        
        if current.right is not None:
            process_queue.append(current.right)
    
    return values


if __name__ == "__main__":
    a = Node('a')
    b = Node('b')
    c = Node('c')
    d = Node('d')
    e = Node('e')
    f = Node('f')
    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f

    #      a
    #    /   \
    #   b     c
    #  / \     \
    # d   e     f

    print(breadth_first_values(a))
    #    -> ['a', 'b', 'c', 'd', 'e', 'f']
    a = Node('a')
    b = Node('b')
    c = Node('c')
    d = Node('d')
    e = Node('e')
    f = Node('f')
    g = Node('g')
    h = Node('h')
    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f
    e.left = g
    f.right = h

    #      a
    #    /   \
    #   b     c
    #  / \     \
    # d   e     f
    #    /       \
    #   g         h

    #print(breadth_first_values(a))
    #   -> ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    a = Node('a')
    #      a

    #print(breadth_first_values(a))
    #    -> ['a']

