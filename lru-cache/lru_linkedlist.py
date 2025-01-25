from typing import List


class ListNode:
    def __init__(self, val, next=None) -> None:
        self.val = val
        self.next = next


class LRUCache:
    def __init__(self) -> None:
        # to maintain the node val.
        self.head = None
        self.cache = dict()

    def put(self, key, val):
        # for existing entry
        if self.get(key) < 0:
            tmp = self.head
            self.head = ListNode(val, tmp)
        self.cache[key] = val

    def get(self, key):
        val = self.cache.get(key, -1)
        if val >= 0:
            tmp = self.head
            self.head = ListNode(val, tmp)
        return val

    def __repr__(self) -> str:
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.val)
            node = node.next
        nodes.append("None")
        return " -> ".join(map(str, nodes))


# Not working

lru = LRUCache()
lru.put(2, 1)
print(lru.cache)
lru.put(1, 5)
print(lru.cache)
lru.put(2, 3)
print(lru.cache)
lru.put(4, 6)
print(lru.cache)
# lru.get(1)
lru.get(2)
print(lru)
