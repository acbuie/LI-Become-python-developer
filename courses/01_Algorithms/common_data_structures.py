# ----- Linked List ----- #

# Node class 
class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None

    def get_data(self):
        return self.val

    def set_data(self, val):
        self.val = val

    def get_next(self):
        return self.next

    def set_next(self, next):
        self.next = next

# Linked List class
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        self.count = 0

    def get_count(self):
        return self.count

    def insert(self, data):
        # TODO insert new node
        new_node = Node(data)

        new_node.set_next(self.head)
        self.head = new_node
        self.count += 1

    def find(self, val):
        # TODO find first item with val
        item = self.head
        while (item != None):
            if item.get_data() == val:
                return item
            else:
                item = item.get_next()

        return None

    def delete_at(self, idx):
        # TODO delete an item at idx
        if idx < self.count - 1:
            return
        if idx == 0:
            self.head = self.head.get_next()
        else:
            temp_idx = 0
            node = self.head
            while temp_idx < idx - 1:
                node = node.get_next()
                temp_idx += 1
            node.set_next(node.get_next().get_next())
            self.count -= 1

    def dump_list(self):
        temp_node = self.head
        while(temp_node != None):
            print('Node: ', temp_node.get_data())
            temp_node = temp_node.get_next()

# Testing 
# itemlist = LinkedList()
# itemlist.insert(38)
# itemlist.insert(49)
# itemlist.insert(13)
# itemlist.insert(15)
# itemlist.dump_list()

# print('Item count: ', itemlist.get_count())
# print('Finding item: ', itemlist.find(13)) # In list
# print('Finding item: ', itemlist.find(78)) # Not in list

# itemlist.delete_at(3)
# print('Item count: ', itemlist.get_count())
# print('Finding item: ', itemlist.find(38)) # Should be deleted
# itemlist.dump_list()

# ----- Stacks ----- # 

"""
How are stacks and queues different?

stack: 
    last in, first out data structure
    last in is the first popped

queues: 
    first in, first out structure
    items generally removed from the front, like a queue
"""

# TODO Create empty stack
stack = []

# TODO Push onto stack
stack.append(1)
stack.append(2)
stack.append(3)
stack.append(4)

# TODO Print stack contents
# print(stack)

# TODO Pop item off stack
stack.pop()
# print(stack)

# ----- Queues ----- #
from collections import deque

# TODO Create empty queue
queue = deque()

# TODO Add items
queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)

# TODO Print queue contents
# print(queue)

# TODO Pop item off queue
queue.popleft() # Pop from the left
# print(queue)

# ----- Hash Tables/Dictionaries ----- #

"""
Key-value mapping, typically very fast
can be unordered, but remember order in python 3.6+ with CPython
"""

# TODO Create hashtable all at once
items_1 = dict({'key1': 1, 'key2': 2, 'key3': 'three'})
# print(items_1)

# TODO Create progressively
items_2 = {}
items_2['key1'] = 1
items_2['key2'] = 2
items_2['key3'] = 'three'
# print(items_2)

# TODO Try to access nonexistent key
# print(items_1['key6'])

# TODO Replace an item
items_2['key2'] = 'two'
# print(items_2)

# TODO Iterate keys and values
for key, value in items_2.items():
    print('key: ', key, 'value: ', value)