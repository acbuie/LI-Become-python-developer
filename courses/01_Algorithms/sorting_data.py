# ----- Sorting Data ----- #

"""
Bubble sort: not very quick
Merge: quicker, uses recursion
Quicksort: recursive, very quick
"""

# ----- Bubble Sort ----- #

"""
Swaps adjacent values so larger ones go towards the end
Not practical, mostly teaching tool
"""

def bubblesort(data):
    # TODO
    # Countdown
    for i in range(len(data) - 1, 0, -1):
        for j in range(i):
            if data[j] > data[j + 1]:
                temp = data[j]
                data[j] = data[j + 1]
                data[j + 1] = temp

        # print('Current state: ', data)

list_1 = [6, 20, 8, 19, 34, 22, 67, 42, 87, 53]
bubblesort(list_1)
# print('Result: ', list_1)

# ----- Merge Sort ----- # 

"""
Breaks data down, sorts smaller sets, and merges them back 
together.
Merging back together involves 'walking' the indices up
Work done during merging
"""

def mergesort(data):
    if len(data) > 1:
        midpoint = len(data) // 2
        left = data[:midpoint]
        right = data[midpoint:]

        # TODO Recursion
        mergesort(left)
        mergesort(right)

        # TODO Perform merging
        i = 0 # left index
        j = 0 # right index
        k = 0 # merged index

        # TODO While both arrays have content
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                data[k] = left[i]
                i += 1
            else:
                data[k] = right[j]
                j += 1
            k += 1

        # TODO If left still has values, add them
        while i < len(left):
            data[k] = left[i]
            i += 1
            k += 1

        # TODO If right still has values, add them 
        while j < len(right):
            data[k] = right[j]
            j += 1
            k += 1

list_2 = [5, 78, 2, 45, 37, 64, 24, 12, 95, 34, 26]

# print(list_2)
mergesort(list_2)
# print(list_2)

# ----- Quicksort ----- # 

"""
Divide and conquer, recursive. Slightly more performant
Alters data in place
Uses a 'pivot point' instead of midpoint:
    if values are smaller than pivot, increment index
    if values are larger than pivot, decrease index until
    its less than the pivot value. where the indexs cross, 
    we swap the index and pivot and split. do it all again
"""

def quicksort(data, first, last):
    if first < last:
        # Find split point
        pivot_ind = partition(data, first, last)

        # Sort two partitions
        quicksort(data, first, pivot_ind - 1)
        quicksort(data, pivot_ind + 1, last)

def partition(data_values, first, last):
    # Choose pivot (in this case, first value)
    pivot_value = data_values[first]

    # Find upper and lower indicies
    lower = first + 1
    upper = last

    # Search for crossing point
    done = False
    while not done:
        # TODO Advance lower index
        while lower <= upper and data_values[lower] <= pivot_value:
            lower += 1

        # TODO Advance uppper index
        while data_values[upper] >= pivot_value and upper >= lower:
            upper -= 1

        # TODO If they cross, we found the split point
        if upper < lower:
            done = True
        else:
            # Exchange values
            temp = data_values[lower]
            data_values[lower] = data_values[upper]
            data_values[upper] = temp

    # When split point is found, exchange pivot value
    temp = data_values[first]
    data_values[first] = data_values[upper]
    data_values[upper] = temp

    # Return split point index
    return upper

list_3 = [6, 78, 93, 22, 26, 63, 15, 38, 34, 41, 13]

# print(list_3)
quicksort(list_3, 0, len(list_3) - 1)
# print(list_3)