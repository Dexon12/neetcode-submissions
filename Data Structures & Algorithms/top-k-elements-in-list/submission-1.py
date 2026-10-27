class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = dict()

        for num in nums:
            seen[num] = seen.get(num, 0) + 1

        return sorted([key for key in seen.keys()], key=lambda x: seen[x], reverse=True)[:k]
