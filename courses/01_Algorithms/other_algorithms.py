# ---- Filtering data with hash tables ----- # 

items = ['apple', 'pear', 'orange', 'banana', 'apple', 
         'orange', 'apple', 'pear', 'banana', 'orange', 
         'apple', 'kiwi', 'pear', 'apple', 'orange ']

# TODO Filtering
fltr = dict()

# TODO Add unique items to hashtable
for key in items:
    fltr[key] = 0

# TODO Create a set from keys in hashtable
result = set(fltr.keys())
# print(result)

# ----- Value counting ----- # 

# TODO Make counter
counter = dict()

# TODO Iterate and count each one
for item in items:
    if (item in counter.keys()):
        counter[item] += 1
    else:
        counter[item] = 1

# print(counter)

# ----- Find max in list ----- # 

values = [6, 20, 8, 19, 56, 23, 87, 41, 49, 53]

def find_max(values):
    # TODO Breaking condiction
    if len(values) == 1:
        return values[0]

    # TODO Get first item, call function on rest of list
    op1 = values[0]
    # print(op1)
    op2 = find_max(values[1:])
    # print(op2)

    # TODO Perform comparison when down to just 2 items
    if op1 > op2:
        return op1
    else:
        return op2

print(find_max(values))