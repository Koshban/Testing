'''
Write a function, tree_sum, that takes in the root of a binary tree that contains number values. The function should return the total sum of all values in the tree.
'''
from BinaryTreeClass import Node
from collections import deque

''' Using DFS iteratively'''
def tree_sum_iterative(root) -> int:
    sum = 0
    if root is None:
        return sum
    
    stack = [root]
    while stack:
        current = stack.pop()
        sum += current.val
        if current.right is not None:
            stack.append(current.right)
        if current.left is not None:
            stack.append(current.left)
    return sum

''' Using DFS Recursively'''
def tree_sum_recursive(root) -> int:
    sum = 0
    if root is None:
        return sum
    
    return root.val + tree_sum_recursive(root.left) + tree_sum_recursive(root.right)

def tree_sum_bfs(root) -> int:
    sum = 0
    if root is None:
        return sum   
    queue = deque([root])
    while queue:
        current = queue.popleft()
        sum += current.val
        if current.left is not None:
            queue.append(current.left)
        
        if current.right is not None:
            queue.append(current.right)
    return sum

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

    #       3
    #    /    \
    #   11     4
    #  / \      \
    # 4   -2     1

    print(tree_sum_bfs(a)) # -> 21
    a = Node(1)
    b = Node(6)
    c = Node(0)
    d = Node(3)
    e = Node(-6)
    f = Node(2)
    g = Node(2)
    h = Node(2)
    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f
    e.left = g
    f.right = h

    #      1
    #    /   \
    #   6     0
    #  / \     \
    # 3   -6    2
    #    /       \
    #   2         2

    print(tree_sum_bfs(a)) # -> 10

    print(tree_sum_bfs(None)) # -> 0





