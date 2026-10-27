class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = dict()

        for num in nums:
            seen[num] = seen.get(num, 0) + 1

        result = []
        sorted_dict = sorted(seen.items(), key=lambda x: x[1], reverse=True)[:k]
        for key, value in sorted_dict:
            result.append(key)

        return result