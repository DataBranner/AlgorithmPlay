# binary_search_naive.py
# 20131023
# David Prager Branner
# Written for Python 3.3

"""Implement a binary search tree with insertion from root and no rebalancing."""

import sys
from collections import deque as D

class Node():
    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.left = None
        self.right = None

def insert(root, node):
    if root.key == None:
        root.key = node.key
    elif node.key <= root.key:
        # insert in this subtree
        if not root.left:
            root.left = node
#            print('inserted', node.key, 'on left')
        else:
            insert(root.left, node)
    else:
        # insert in this subtree
        if not root.right:
            root.right = node
#            print('inserted', node.key, 'on right')
        else:
            insert(root.right, node)

def preorder_traverse(root, output=None):
    if not output:
        output = []
    if root:
        output.extend([root.key])
        output = preorder_traverse(root.left, output)
        output = preorder_traverse(root.right, output)
    return output

def inorder_traverse(root, output=None):
    if not output:
        output = []
    if root:
        output = inorder_traverse(root.left, output)
        output.extend([root.key])
        output = inorder_traverse(root.right, output)
    return output

def postorder_traverse(root, output=None):
    if not output:
        output = []
    if root:
        output = postorder_traverse(root.left, output)
        output = postorder_traverse(root.right, output)
        output.extend([root.key])
    return output

def breadthfirst_traverse(root):
    output = []
    queue = D([root])
    while queue:
        root = queue.popleft()
        output.append(root.key)
        if root.left:
            queue.extend([root.left])
        if root.right:
            queue.extend([root.right])
    return output

def min(root):
    if not root:
        return None
    elif root.left:
        return min(root.left)
    else:
        return root.key

def max(root):
    if not root:
        return None
    elif root.right:
        return max(root.right)
    else:
        return root.key

def populate_tree(keys=None, data=None):
    if not keys:
        root = None
    else:
        if not all(isinstance(i, int) for i in keys):
            print('\nOnly integers are allowed as keys.\nExiting.')
            sys.exit(1)
        if not data:
            data = [None for i in range(len(keys))]
        root = Node(keys[0], data[0])
        for key, datum in zip(keys[1:], data[1:]):
            node = Node(key, datum)
            insert(root, node)
    return root
