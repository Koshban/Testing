'''
Write a function, tree_includes, that takes in the root of a binary tree and a target value. The function should return a boolean indicating whether or not the value is contained in the tree.
'''
from BinaryTreeClass import Node
from collections import deque

''' Using DFS iteratively'''

def tree_includes_iterative(root, target: str) -> bool:

    if root is None or target is None:
        return None
    
    stack = [ root ]
    while stack:
        current = stack.pop()
        if current.val == target:
            return True
        
        if current.left is not None:
            stack.append(current.left)

        if current.right is not None:
            stack.append(current.right)
    return False


''' Using DFS recursively'''

def tree_includes_recursively(root, target: str) -> bool:

    if root is None or target is None:
        return False
    
    if root.val == target:
        return True
    
    return ( tree_includes(root.left,target ) or tree_includes(root.right, target) )


''' Using BFS '''

def tree_includes(root, target: str) -> bool:
    if root is None or target is None:
        return False
    
    queue = deque([ root ])
    while queue:
        current = queue.popleft()
        if current.val == target:
            return True
        
        if current.left is not None:
            queue.append(current.left)
        
        if current.right is not None:
            queue.append(current.right)
    
    return False

if __name__ == "__main__":
    a = Node("a")
    b = Node("b")
    c = Node("c")
    d = Node("d")
    e = Node("e")
    f = Node("f")
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
    print(tree_includes(a, "e")) # -> True

    a = Node("a")
    b = Node("b")
    c = Node("c")
    d = Node("d")
    e = Node("e")
    f = Node("f")
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
    print(tree_includes(a, "a")) # -> True

    a = Node("a")
    b = Node("b")
    c = Node("c")
    d = Node("d")
    e = Node("e")
    f = Node("f")
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
    print(tree_includes(a, "n")) # -> False


