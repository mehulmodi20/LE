class Stack:
    def __init__(self):
        self._item = []

    def push(self, item):
        return self._item.append(item)

    def pop(self):
        return self._item.pop(-1)

    def peek(self):
        return self._item[-1]

    def size(self):
        return len(self._item)
