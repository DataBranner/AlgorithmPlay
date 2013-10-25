# binary_search_naive.py
# 20131023
# David Prager Branner
# Written for Python 3.3

"""Implement a binary search tree with insertion from root and no rebalancing."""

from collections import deque as D

class Node():
    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.left = None
        self.right = None

def insert(root, node):
    if not root.key:
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
#        print('  now have root.key:', root.key)
        output.append(root.key)
#        print(output)
#        print('queue:', [i.key for i in queue])
        if root.left:
            queue.extend([root.left])
#            print('  adding', root.left.key)
        if root.right:
            queue.extend([root.right])
#            print('  adding', root.right.key)
    return output

def populate_tree(key):
    root = Node(key[0], 0)
    for item in key[1:]:
        node = Node(item, 0)
        insert(root, node)
    return root
