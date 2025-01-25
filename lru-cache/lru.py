from collections import OrderedDict


class LRUCache:

    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        try:
            self.cache[key]
        except KeyError:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        # remove last item from the cache if capacity is reached.
        if self.cache.get(key, None):
            self.cache[key] = value
            self.cache.move_to_end(key)
            return
        if len(self.cache) == self.capacity:
            self.cache.popitem(last=False)
        self.cache[key] = value


# ["LRUCache","put","put","put","put","get","get"]
# [[2],[2,1],[1,1],[2,3],[4,1],[1],[2]]

# lru = LRUCache(2)
# lru.put(2, 1)
# print(lru.cache)
# lru.put(1, 1)
# print(lru.cache)
# lru.put(2, 3)
# print(lru.cache)
# lru.put(4, 1)
# print(lru.cache)
# lru.get(1)
# lru.get(2)

lru = LRUCache(4)
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
# print(lru)
