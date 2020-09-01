# ----- Unordered Search ----- #

"""
Sometimes called linear search
Have to search item-wise
"""

def find_item(item, list):
    # TODO Search item-wise
    for i in range(0, len(list)):
        if item == list[i]:
            return i
    
    # If item is not found
    return None

list_1 = [3, 5, 21, 6, 20, 63, 22, 8, 52, 41]
print(list_1)
print(find_item(52, list_1))
print(find_item(33, list_1))