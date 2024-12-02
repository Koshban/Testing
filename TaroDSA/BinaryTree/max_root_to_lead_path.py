'''
Write a function, max_path_sum, that takes in the root of a binary tree that contains number values. The function should return the maximum sum of any root to leaf path within the tree.

You may assume that the input tree is non-empty.
'''
from BinaryTreeClass import Node

# Iterrative solution
# def max_path_sum(root) -> int:
#     maxpathsum = float('-inf')
#     if root is None:
#         return maxpathsum
#     stack = [root]
#     while stack:
#         current = stack.pop()
#         maxpathsum = max(maxpathsum, current.val )

#         if current.left is not None:
#             stack.append(current.left)

#         if current.right is not None:
#             stack.append(current.right)
    
#     return maxpathsum

#Recursive solution
def max_path_sum(root) -> int:
    if root is None:
        return float('-inf')
    if root.left is None and root.right is None:
        return root.val
    
    return root.val + max(max_path_sum(root.left), max_path_sum(root.right))


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
    print(max_path_sum(a)) # -> 18


    a = Node(5)
    b = Node(11)
    c = Node(54)
    d = Node(20)
    e = Node(15)
    f = Node(1)
    g = Node(3)
    a.left = b
    a.right = c
    b.left = d
    b.right = e
    e.left = f
    e.right = g
    #       5
    #     /   \
    #    11   54
    #  /   \
    # 20   15
    #      / \
    #     1   3
    print(max_path_sum(a)) # -> 59
