# ----- Unordered Search ----- #

"""
Sometimes called linear search
Have to search item-wise
Linear time
"""

def find_item(item, list):
    # TODO Search item-wise
    for i in range(0, len(list)):
        if item == list[i]:
            return i
    
    # If item is not found
    return None

list_1 = [3, 5, 21, 6, 20, 63, 22, 8, 52, 41]
# print(list_1)
# print(find_item(52, list_1))
# print(find_item(33, list_1))

# ----- Ordered Search ----- # 

"""
Binary search. check if midpoint is our value. if not, increase or 
decrease index of lower, find new midpoint, repeat
Log time
"""

def binary_search(item, list):
    list_size = len(list) - 1

    # Two endpoints
    lower = 0
    upper = list_size

    while lower <= upper:
        # TODO Find midpoint
        midpoint = (lower + upper) // 2

        # TODO If found, return index
        if list[midpoint] == item:
            return midpoint

        # TODO Get next midpoint
        if item > list[midpoint]:
            lower = midpoint + 1
        else:
            upper = midpoint - 1

    # If indices cross, exit. Value not in list
    if lower > upper:
        return None

list_2 = [4, 7, 22, 53, 75, 79, 86, 103, 122]

# print(binary_search(86, list_2))
# print(binary_search(24, list_2))

# ----- Determine if sorted ----- # 

def is_sorted(list):
    # TODO Brute force it
    for i in range(len(list) - 1):
        if list[i] > list[i + 1]:
            return False

    return True

def is_sorted_py(list):
    # TODO Pythonic way
    
    return all(list[i] <= list[i + 1] for i in range(len(list) - 1))


print(is_sorted_py(list_1)) # Not
print(is_sorted_py(list_2)) # Sorted