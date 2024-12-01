class Node:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None


a = Node('A')
b = Node('B')
c = Node('C')
d = Node('D')
e = Node('E')
f = Node('F')
g = Node('G')
h = Node('H')

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
c.left = g
d.left = h


#                    A
#                  / \
#                  B   C
#                  /\  /\
#                 D  E G F
#                /
#                H
