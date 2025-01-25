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


class OrderedLists:
    def __init__(self):
        self.head = None

    def add(self, item):
        """Add a new node"""
        current = self.head
        previous = None
        temp = Node(item)

        while current is not None and current._data < item:
            previous = current
            current = current.next

        if previous is None:
            temp.next = self.head
            self.head = temp
        else:
            temp.next = current
            previous.next = temp

    def __str__(self):
        current = self.head
        s = str(current._data) + ','
        while current.next is not None:
            current = current.next
            s += str(current._data) + ','
        return s


my_list = OrderedLists()
my_list.add(17)
my_list.add(26)
my_list.add(31)
my_list.add(54)
my_list.add(77)
my_list.add(93)
my_list.add(22)
print(my_list)
