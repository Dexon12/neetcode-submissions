class MyHashMap:

    def __init__(self):
        self.hash_counts = 769
        self.containers = [[] for _ in range(self.hash_counts)]

    def _hash(self, val: int) -> int:
        return val % self.hash_counts

    def put(self, key: int, value: int) -> None:
        index = self._hash(val=key)
        container = self.containers[index]
        
        for i, (k, v) in enumerate(container):
            if key == k:
                container[i] = (key, value)
                return
        container.append((key, value))

    def get(self, key: int) -> int:
        index = self._hash(val=key)
        container = self.containers[index]
        
        for i, (k, v) in enumerate(container):
            if key == k:
                return v
        
        return -1

    def remove(self, key: int) -> None:
        index = self._hash(val=key)
        container = self.containers[index]
        
        for i, (k, v) in enumerate(container):
            if key == k:
                del container[i]
                return

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)