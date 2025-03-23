# '''
# Write a function, depth_first_values, that takes in the root of a binary tree. The function should return a list containing all values of the tree in depth-first order.

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

# depth_first_values(a)  -> ['a', 'b', 'd', 'e', 'c', 'f']
# '''
from BinaryTreeClass import Node

# Iterrative solution
def depth_first_values_iterative(root):
    values= []
    if root is None: # Empty Tree
        return values
    stack = [root]
    while stack: # While its not empty its truthy
        current = stack.pop() 
        values.append(current.val)
        
        if current.right is not None:
            stack.append(current.right)
        
        if current.left is not None:
            stack.append(current.left)
    
    return values

# recursive solution
def depth_first_values(root):
    values= []
    if root is None: # Empty Tree
        return values
    
    left_values = depth_first_values(root=root.left)
    print(left_values)
    right_values = depth_first_values(root=root.right)
    print(right_values)

    #return [root.val, *left_values, *right_values]
    return [root.val] + left_values + right_values
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
    print(depth_first_values(a))

    a = Node('a')
    b = Node('b')
    c = Node('c')
    d = Node('d')
    e = Node('e')
    f = Node('f')
    g = Node('g')
    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f
    e.left = g
    #      a
    #    /   \
    #   b     c
    #  / \     \
    # d   e     f
    #    /
    #   g

    print(depth_first_values(a))     #   -> ['a', 'b', 'd', 'e', 'g', 'c', 'f']
    a = Node('a')
    #     a

    print(depth_first_values(a))    #   -> ['a']
    print(depth_first_values(None))    #   -> []
    
