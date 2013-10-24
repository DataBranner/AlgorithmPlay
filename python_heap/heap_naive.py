# heap_naive.py
# 20131023
# David Prager Branner
# Written for Python 3.3

"""Implement a heap with insertion from root and no rebalancing."""

from collections import deque as D

class Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def insert(root, node):
    if not root.data:
        root.data = node.data
    elif node.data <= root.data:
        # insert in this subtree
        if not root.left:
            root.left = node
#            print('inserted', node.data, 'on left')
        else:
            insert(root.left, node)
    else:
        # insert in this subtree
        if not root.right:
            root.right = node
#            print('inserted', node.data, 'on right')
        else:
            insert(root.right, node)

def preorder_traverse(root, output=[]):
    if not output:
        output = []
    if root:
        output.extend([root.data])
        output = preorder_traverse(root.left, output)
        output = preorder_traverse(root.right, output)
    return output

def inorder_traverse(root, output=[]):
    if not output:
        output = []
    if root:
        output = inorder_traverse(root.left, output)
        output.extend([root.data])
        output = inorder_traverse(root.right, output)
    return output

def postorder_traverse(root, output=[]):
    if not output:
        output = []
    if root:
        output = postorder_traverse(root.left, output)
        output = postorder_traverse(root.right, output)
        output.extend([root.data])
    return output

def breadthfirst_traverse(root):
    output = []
    queue = D([root])
    while queue:
        root = queue.popleft()
#        print('  now have root.data:', root.data)
        output.append(root.data)
#        print(output)
#        print('queue:', [i.data for i in queue])
        if root.left:
            queue.extend([root.left])
#            print('  adding', root.left.data)
        if root.right:
            queue.extend([root.right])
#            print('  adding', root.right.data)
    return output

def populate_tree(data):
    root = Node(data[0])
    for item in data[1:]:
        node = Node(item)
        insert(root, node)
    return root
