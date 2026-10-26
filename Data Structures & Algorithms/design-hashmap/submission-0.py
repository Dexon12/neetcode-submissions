class MyHashMap:

    def __init__(self):
        self.hash_counts = 769
        self.containers = [[] for _ in range(self.hash_counts)]

    def _hash(self, val: int) -> int:
        return val % self.hash_counts

    def put(self, key: int, value: int) -> None:
        index = self._hash(val=key)
        container = self.containers[index]
        
        if key in container:
            key_index = container.index(key)
            container[key_index+1] = value
        else:
            container.append(key)
            container.append(value)

    def get(self, key: int) -> int:
        index = self._hash(val=key)
        container = self.containers[index]
        
        if key in container:
            key_index = container.index(key)
            return container[key_index+1]
        else:
            return -1

    def remove(self, key: int) -> None:
        index = self._hash(val=key)
        container = self.containers[index]

        if key in container:
            key_index = container.index(key)
            print(container, key_index, key_index+1)
            del container[key_index+1]
            del container[key_index]



# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)