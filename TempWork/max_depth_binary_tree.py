''' Given a binary tree, write a function to calculate the maximum depth (height) of the tree.'''
import unittest
from typing import Optional
from collections import deque

class Node:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None

def print_tree(root: Optional[Node]) -> None:
    """Print tree level by level with proper formatting"""
    if not root:
        print("Empty Tree")
        return
    
    # Use queue for level order traversal
    queue = deque([(root, 0)])
    curr_level = 0
    level_nodes = []
    
    while queue:
        node, level = queue.popleft()
        
        # Start new level
        if level > curr_level:
            print(' '.join(map(str, level_nodes)))
            level_nodes = []
            curr_level = level
        
        # Add node value or placeholder
        level_nodes.append(str(node.val) if node else '_')
        
        # Add children to queue
        if node:
            queue.append((node.left, level + 1))
            queue.append((node.right, level + 1))
    
    # Print last level
    if level_nodes:
        print(' '.join(map(str, level_nodes)))
    print("-" * 20)  # Separator

def max_depth(root: Node) -> int:
    if root is None:
        return 0
        
    left_depth = max_depth(root.left)
    right_depth = max_depth(root.right)
    
    return max(left_depth, right_depth) + 1

class TestMaxDepth(unittest.TestCase):
    def setUp(self):
        # Test Case 1: Single node
        self.tree1 = Node(1)
        
        # Test Case 2: Simple tree with depth 2
        self.tree2 = Node(1)
        self.tree2.left = Node(2)
        self.tree2.right = Node(3)
        
        # Test Case 3: Unbalanced tree
        self.tree3 = Node(1)
        self.tree3.left = Node(2)
        self.tree3.left.left = Node(4)
        self.tree3.left.left.left = Node(5)
        
        # Test Case 4: Complete binary tree
        self.tree4 = Node(1)
        self.tree4.left = Node(2)
        self.tree4.right = Node(3)
        self.tree4.left.left = Node(4)
        self.tree4.left.right = Node(5)
        self.tree4.right.left = Node(6)
        self.tree4.right.right = Node(7)

    def test_max_depth(self):
        test_cases = [
            {
                'input': None,
                'expected': 0,
                'description': 'Empty tree'
            },
            {
                'input': self.tree1,
                'expected': 1,
                'description': 'Single node tree'
            },
            {
                'input': self.tree2,
                'expected': 2,
                'description': 'Simple tree with depth 2'
            },
            {
                'input': self.tree3,
                'expected': 4,
                'description': 'Unbalanced tree'
            },
            {
                'input': self.tree4,
                'expected': 3,
                'description': 'Complete binary tree'
            }
        ]

        for test_case in test_cases:
            with self.subTest(test_case=test_case):
                print(f"\nTesting: {test_case['description']}")
                print("Tree structure:")
                print_tree(test_case['input'])
                
                actual = max_depth(test_case['input'])
                print(f"Expected depth: {test_case['expected']}")
                print(f"Actual depth: {actual}")
                
                self.assertEqual(
                    actual,
                    test_case['expected'],
                    f"Failed {test_case['description']}: expected {test_case['expected']}, got {actual}"
                )

if __name__ == '__main__':
    unittest.main(verbosity=2)

