#! /usr/bin/env python
# sort_mixed_list.py
# David Prager Branner
# 20140605, works

from collections import deque

def main(lst):
    # Assign template
    template = [type(i) for i in lst]
    # Find datatypes present
    datatypes = set(template)
    # Create distinct list for each datatype (use dict)
    list_dict_by_type = {}
    for i in lst:
        if type(i) not in list_dict_by_type:
            list_dict_by_type[type(i)] = []
        list_dict_by_type[type(i)].append(i)
    # Sort each list
    list_dict_by_type = {i: deque(insertionsort(list_dict_by_type[i])) 
            for i in list_dict_by_type}
    # Recombine distinct lists into one, following template
    recombined_list = [list_dict_by_type[i].popleft() for i in template]
    return recombined_list

def insertionsort(lst):
    lst.sort()
    for i in range(len(lst)):
        while i > 0 and lst[i] < lst[i - 1]:
            lst[i], lst[i - 1] = lst[i - 1], lst[i]
            i -= 1
    return lst
