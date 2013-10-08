# sorting.py
# 20130912
# David Prager Branner
'''Various sorting algorithms implemented in Python for study purposes.'''

def find_index_closest_to_mean(the_list):
    '''Find value closest to mean of largest and smallest values in the_list.'''
    # This was intended for use finding a quicksort pivot, but proved to be of
    # no use increasing speed.
    #
    # Traverse list, identify largest and smallest members; find their mean
    smallest = the_list[0]
    largest = the_list[0]
    for i in the_list[1:]:
        if i < smallest:
            smallest = i
        elif i > largest:
            largest = i
    rough_mean = (largest + smallest)/2
    # Traverse list again, identify member w/ smallest abs distance from mean
    middlest = the_list[0]
    index = 0
    previous_distance = abs(rough_mean - middlest)
    for i, item in enumerate(the_list[1:]):
        distance = abs(rough_mean - item)
        if distance < previous_distance:
            middlest = item
            index = i
            previous_distance = distance
    return index+1, middlest

def quicksort(the_list):
    '''Quicksort: choose pivot and divide into elements > or <= pivot; call
    recursively.'''
    # Recursion returns
    if not the_list:
        return the_list
    #
    # Divide, using the_list[0] as pivot
    # Note: no particular speed improvement using array.array instead of list.
    first_half = []
    second_half = []
    for item in the_list[1:]:
        if item < the_list[0]:
            first_half.append(item)
        else:
            second_half.append(item)
    #
    # Recursive call and recombination
    return quicksort(first_half) + list([the_list[0]]) + quicksort(second_half)

def mergesort(the_list):
    '''Mergesort: subdivide list and recombine in order by size.'''
    # Return from bottom of recursion.
    if len(the_list) == 1:
        return the_list
    #
    # Divide array and send halves to recursion.
    length_whole = len(the_list)
    halfway_index = length_whole // 2
    first_half = mergesort(the_list[0:halfway_index])
    second_half = mergesort(the_list[halfway_index:])
    #
    # Recombine;
    # since lists are expensive to head-pop, use cursors to traverse them.
    curs1 = 0
    curs2 = 0
    the_sorted_list = []
    while len(the_sorted_list) < length_whole:
        # First eliminate cases where one list is exhausted.
        if curs1 == len(first_half):
            the_sorted_list.extend(second_half[curs2:])
        elif curs2 == len(second_half):
            the_sorted_list.extend(first_half[curs1:])
        # Now use cursors to compare current index of each list;
        # must then increment relevant cursor.
        elif first_half[curs1] < second_half[curs2]:
            the_sorted_list.append(first_half[curs1])
            curs1 += 1
        else:
            the_sorted_list.append(second_half[curs2])
            curs2 += 1
    return the_sorted_list

def insertionsort1(the_list):
    '''Abandoned.'''
    for i in range(len(the_list[1:])+1):
        for j in range(len(the_list[0:i])):
            if the_list[i] < the_list[j]:
                the_list[i], the_list[j] = the_list[j], the_list[i]
    return the_list

def insertionsort(the_list):
    '''Traverse the list and compare each item with the previous one, swapping
    them if necessary to put them in ranked order; if swapped, the comparison
    must continue item by item until the current item is in the correct
    place.'''
    # Traverse list.
    for i in range(len(the_list)):
        # Use a dummy cursor because its value must change in the case of a
        # swap.
        cursor_main = i
        # Using a variable for the main candidate item is not necessary but
        # saves time.
        main_candidate = the_list[cursor_main]
        # Compare item with each previous item, working backward.
        for j in range(i, 0, -1):
            transient_tested = the_list[j-1]
            # Stop comparisons if current item is in correct rank.
            if transient_tested < main_candidate:
                break
            else:
                # Swap items and reset dummy cursor.
                the_list[cursor_main], the_list[j-1] = \
                        transient_tested, main_candidate
                cursor_main = j-1
    return the_list

def zadrozny_insertionsort(the_list):
    '''Matthew Zadrozny's version. Slightly slower than insertionsort().'''
    for i, val in enumerate(the_list):
        temp = i
        while temp != 0 and the_list[temp] < the_list[temp-1]:
            the_list[temp], the_list[temp-1] = the_list[temp-1], the_list[temp]
            temp -= 1
    return the_list
