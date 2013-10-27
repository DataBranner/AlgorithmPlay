# binary_search_naive.py
# 20131023
# David Prager Branner
# Written for Python 3.3

"""
Implement a binary search tree with insertion from root and no rebalancing.

Requirements:
    1. List of keys must be integers only and have no duplicates
    2. List of data must be of the same cardinality as list of keys.
"""

import sys
from collections import deque as D

class Node():
    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.left = None
        self.right = None
        self.parent = None

def insert(root, node):
    if root.key == None:
        root.key = node.key
    elif node.key < root.key:
        # insert in this subtree
        if not root.left:
            root.left = node
            root.left.parent = root
        else:
            insert(root.left, node)
    elif node.key > root.key:
        # insert in this subtree
        if not root.right:
            root.right = node
            root.right.parent = root
        else:
            insert(root.right, node)
    else:
        # key already exists
        pass

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
    """Return leftmost node."""
    if not root:
        return None
    elif root.left:
        return min(root.left)
    else:
        return root

def max(root):
    """Return rightmost node."""
    if not root:
        return None
    elif root.right:
        return max(root.right)
    else:
        return root

def search(root, to_find):
    """Return the node containing to_find."""
    if root.key == to_find:
        return root
    elif root.left and to_find < root.key:
        return search(root.left, to_find)
    elif root.right and to_find > root.key:
        return search(root.right, to_find)
    else:
        return None

def delete(root, to_delete):
    """Find and delete node with desired to_delete."""
    node = search(root, to_delete)
    if not node:
        return
    #
    # Case 1: node that is a leaf.
    if not (node.left and node.right):
        print('    Case 1')
        # If node is root, tree without node is empty.
        if not node.parent:
            return None
        # Set to None parent's child that held the value "to_delete".
        elif to_delete < node.parent.key:
            node.parent.left = None
        else:
            node.parent.right = None
        # Node to return remains root.
    #
    # Case 2: node that has only one child.
    #    Case 2a. Node has only left child, which will replace it.
    elif not node.right:
        print('    Case 2a')
        # 2ai. If node is not root, then parent's pointer to node is changed
        #    to node's left child.
        if node.parent:
            node.parent = fix_parent_link_to_node(node, node.left)
#             if node.parent.left == node:
#                 node.parent.left = node.left
#             elif node.parent.right == node:
#                 node.parent.right = node.left
        # 2aii. But if node is root, then node's sole child becomes root.
        else:
            return node.left
    #    Case 2b. Node has only right child, which will replace it.
    elif not node.left:
        print('    Case 2b')
        # 2bi. If node is not root, then parent's pointer to node is changed
        #    to node's right child.
        if node.parent:
            node.parent = fix_parent_link_to_node(node, node.right)
#             if node.parent.left == node:
#                 node.parent.left = node.right
#             elif node.parent.right == node:
#                 node.parent.right = node.right
        # 2bii. But if node is root, then node's sold child becomes root.
        else:
            return node.right
    #
    # Case 3: node has two children.  Replace with maximum node in left 
    #    subtree.
    else:
        print('    Case 3')
        # 3a. Get maximum node in left subtree as "replacement".
        replacement = max(node.left)
        print('    node:', node.key, 'replacement:', replacement.key)
        # 3b. If replacement has child (must be left), fix replacement's 
        #    parent so that its right child (necessarily right) points to 
        #    replacement's child.
        if replacement.left:
            replacement.parent.right = replacement.left
        # 3b. Replacement takes on node's children.
        replacement.right = node.right
        if node.left != replacement:
            replacement.left = node.left
        # 3c. If node is not root, then parent's pointer to node is changed to
        # replacement.
        if node.parent:
            node.parent = fix_parent_link_to_node(node, replacement)
        # 3d. But if node is root, then node's sole child becomes root.
        else:
            return replacement
    #
    # If we are here, then tree is changed but root is unchanged.
    return root

def fix_parent_link_to_node(node, replacement):
    """Take parent's link to node and set it to replacement."""
    # Assumes parent exists
    if node.parent.left == node:
        node.parent.left = replacement
    elif node.parent.right == node:
        node.parent.right = replacement
    return node.parent


def check_for_fatal_issues(keys, data):
    if not all(isinstance(i, int) for i in keys):
        sys.exit('\nOnly integers are allowed as keys.\nExiting.')
    elif len(set(keys)) != len(keys):
        sys.exit('\nAll keys must be unique.\nExiting.')
    elif len(keys) !=len(data):
        sys.exit('''\nWe have {} keys and {} pieces of data; '''
            '''they must be the same.\nExiting'''.
            format(len(keys), len(data)))

def populate_tree(keys=None, data=None):
    """Returns root node of populated tree."""
    if not keys:
        return None
    if not data:
        data = [None for i in range(len(keys))]
    check_for_fatal_issues(keys, data)
    root = Node(keys[0], data[0])
    for key, datum in zip(keys[1:], data[1:]):
        node = Node(key, datum)
        insert(root, node)
    return root
