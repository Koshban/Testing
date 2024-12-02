'''
Write a function, tree_min_value, that takes in the root of a binary tree that contains number values.

The function should return the minimum value within the tree.

You may assume that the input tree is non-empty.
'''
from BinaryTreeClass import Node
from collections import deque

''' Using DFS iteratively'''

def tree_min_value_iteratively(root) -> int:
    if root is None:
        return 0
    stack, minval = [], float('inf')
    stack = [ root]
    while stack:
        current = stack.pop()
        minval = min(current.val, minval)
        if current.left is not None:
            stack.append(current.left)
        
        if current.right is not None:
            stack.append(current.right)
    return minval


''' Using DFS recursively'''

def tree_min_value_recursively(root) -> int:
    minval = float('inf')
    if root is None:
        return minval

    return min(root.val, tree_min_value_recursively(root=root.left), tree_min_value_recursively(root=root.right))

''' Using BFS '''

def tree_min_value(root) -> int:
    if root is None:
        return 0
    minval = float('inf')
    queue = deque([ root ])
    while queue:
        current = queue.popleft()
        minval = min(minval, current.val)
        if current.left is not None:
            queue.append(current.left)
        
        if current.right is not None:
            queue.append(current.right)
    return minval  

if __name__ == "__main__":
    a = Node(3)
    b = Node(11)
    c = Node(4)
    d = Node(4)
    e = Node(-2)
    f = Node(1)
    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f
    #      3
    #    /   \
    #   11    4
    #  / \     \
    # 4   -2    1
    print(tree_min_value(a)) # -> -2

    a = Node(5)
    b = Node(11)
    c = Node(3)
    d = Node(4)
    e = Node(14)
    f = Node(12)
    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f
    #      5
    #    /   \
    #   11    3
    #  / \     \
    # 4   14    12
    print(tree_min_value(a)) # -> 3

    a = Node(-1)
    b = Node(-6)
    c = Node(-5)
    d = Node(-3)
    e = Node(-4)
    f = Node(-13)
    g = Node(-2)
    h = Node(-2)
    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f
    e.left = g
    f.right = h
    #        -1
    #      /   \
    #    -6    -5
    #   /  \     \
    # -3   -4   -13
    #      /       \
    #    -2        -2
    print(tree_min_value(a)) # -> -13

