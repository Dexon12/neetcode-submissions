class MyHashSet:

    def __init__(self):
        self.bucket_size = 769
        self.buckets = [[] for _ in range(self.bucket_size)]

    def _hash(self, key: int) -> int:
        return key % self.bucket_size

    def add(self, key: int) -> None:
        key_index = self._hash(key)
        bucket = self.buckets[key_index]

        if key not in bucket:
            bucket.append(key)

    def remove(self, key: int) -> None:
        key_index = self._hash(key)
        bucket = self.buckets[key_index]

        if key in bucket:
            bucket.remove(key)

    def contains(self, key: int) -> bool:
        key_index = self._hash(key)
        bucket = self.buckets[key_index]

        return key in bucket


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)