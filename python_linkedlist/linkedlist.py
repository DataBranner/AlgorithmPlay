# linkedlist.py
# David Prager Branner
# 20131117

"""
Implement simple linked list using Python hash table.

List is created populated (with at least one item); if it becomes empty it is
deleted.

Key: hex value, generated at random
Value: tuple: (datum, next_node).

Nodes are accessed by their keys. The whole list is accessed by root.
Node traversal: set cursor at root; move cursor to key of next node; continue.
The end of the list is None.

Not yet implemented: insert_at_head, doubly linked or circular lists.

"""

import random

class LinkedList():
    def __init__(self, datum, kind = None):
        """Initialize non-empty linked list."""
        self.llist = {}
        # Special kinds of linked list.
        self.kind = kind
        self.kinds = {None, 'doublylinked', 'circular'}
        self.node_max_int = 10000000
        # Get initial key.
        self.root = None
        # If datum is list or string, insert it as sequence, index by index.
        if datum.__class__ in set([list, str]):
            prior_node = None
            for item in datum:
                prior_node = self.insert(item, prior_node)
        else:
            # Initialize non-empty list with single datum.
            self.llist[self.root] = (datum, None)

    def insert(self, datum, prior_node = None):
        """Insert datum in new root node unless prior_node given; return key."""
        # Create node key
        key = hex(random.randint(1, self.node_max_int))
        while key in self.llist:
            key = hex(random.randint(1, self.node_max_int))
        # If prior_node, then find prior_node; else insert at root.
        if prior_node:
            # Set next_node attribute of new node to that of prior_node.
            self.llist[key] = (datum, self.llist[prior_node][1])
            print('self.llist[key]:', self.llist[key])
            # Replace prior_node, setting next_node attribute to new node key,
            # but retaining datum.
            self.llist[prior_node] = (self.llist[prior_node][0], key)
            print('self.llist[prior_node]:', self.llist[prior_node])
        else:
            # Point root to new key, with next node as former root.
            self.llist[key] = (datum, self.root)
            self.root = key
            print('set self.root =', key)
        return key

    def delete(self, datum):
        """Find first node containing datum and delete."""
        # Find first node containing datum.
        cursor = self.root
        prior_node = None
        while cursor:
            if self.llist[cursor][0] == datum:
                break
            else:
                prior_node = cursor
                cursor = self.llist[cursor][1]
        if not cursor:
            return
        # Link prior node to following node.
        if prior_node:
            self.llist[prior_node] = (self.llist[prior_node][0],
                    self.llist[cursor][1])
        else:
            self.root = self.llist[cursor][1]
        # Delete found node.
        del self.llist[cursor]
        # If list is now empty, delete hash table.
        self.destroy_on_empty()
        return cursor

    def destroy_on_empty(self):
        """If list is empty, destroy it."""
        if not self.root:
            del self.llist, self.root

    def find(self, datum):
        """Find and return first node containing datum."""
        # Traverse until node contains datum.
        cursor = self.root
        while cursor:
            if self.llist[cursor][0] == datum:
                return cursor
            else:
                cursor = self.llist[cursor][1]

    def length(self):
        """Traverse list, counting nodes; return final count."""
        counter = 0
        cursor = self.root
        while cursor:
            cursor = self.llist[cursor][1]
            counter += 1
        return counter

    def print(self, verbose = False):
        """Traverse list and print each node in order."""
        cursor = self.root
        key_to_print = ''
        end_line = ' '
        if cursor:
            if verbose:
                key_to_print = cursor + ': '
                end_line = '\n'
            print('{}{}'.format(
                key_to_print, self.llist[cursor][0]), end = end_line)
            cursor = self.llist[cursor][1]
        while cursor:
            if verbose:
                key_to_print = cursor + ': '
                end_line = '\n'
            print('=> {}{}'.format(
                key_to_print,  self.llist[cursor][0]), end = end_line)
            cursor = self.llist[cursor][1]

    def garbage_collect(self):
        """Eliminate any unlinked nodes."""
        # Make set of all keys in traversal
        reachable = set()
        cursor = self.root
        while cursor:
            reachable.add(cursor)
            cursor = self.llist[cursor][1]
        # Find symmetric difference between set of reachable keys and
        #   set of all keys. Then, for each item in difference, remove
        #   from hash table.
        for item in reachable.symmetric_difference(set(self.llist.keys())):
            del self.llist[item]
        # If list is now empty, destroy.
        self.destroy_on_empty()

    def return_list(self):
        """Return as Python list."""
        cursor = self.root
        to_return = []
        while cursor:
            to_return.append(self.llist[cursor][0])
            cursor = self.llist[cursor][1]
        return to_return
