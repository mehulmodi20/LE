#!/usr/bin/env python3.9

class Node:
    def __init__(self, data):
        self._data = data
        self._next = None

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, node):
        self._next = node


class UnorderedLists:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head == None

    '''
    Recall that the linked list structure provides us with only one entry point, the head of the list. All of the other nodes can only be reached by accessing the first node and then following next links. This means that the easiest place to add the new node is right at the head, or beginning, of the list. In other words, we will make the new item the first item of the list and the existing items will need to be linked to this new first item so that they follow.
    '''

    def add(self, data):
        item = Node(data)
        if self.head is None:
            self.tail = item
        item.next = self.head
        self.head = item

    '''
    '''

    def remove(self, data):
        current = self.head
        prev = None

        while current.next != None:
            if current._data == data:
                break
            prev = current
            current = current.next

        if current is None:
            raise ValueError("item not found")
        if prev == None:
            self.head = current.next
        else:
            prev.next = current.next
            if prev.next is None:
                self.tail = prev

    def __str__(self):
        current = self.head
        s = str(current._data) + ','
        while current.next is not None:
            current = current.next
            s += str(current._data) + ','
        return s

    '''
    append with O(n)
    '''

    def append(self, data):

        current = self.head
        new_node = Node(data)
        while current.next is not None:
            current = current.next
        current.next = new_node

    '''
    append with O(1) using self.tail property.
    '''

    def new_append(self, data):
        current_tail = self.tail
        new_node = Node(data)
        current_tail.next = new_node
        self.tail = new_node


my_list = UnorderedLists()
my_list.add(31)
my_list.add(77)
my_list.add(17)
my_list.add(93)
my_list.add(26)
my_list.add(54)

print(my_list)
my_list.remove(17)
print(my_list)
my_list.remove(54)
print(my_list)
my_list.remove(31)
print(my_list)
my_list.append(30)
print(my_list)
my_list.new_append(35)
print(my_list)
my_list.remove(35)
my_list.new_append(40)
print(my_list)
