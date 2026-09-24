class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i in range(len(nums)):
            need_num = target - nums[i]

            if need_num in seen:
                return [seen[need_num], i]

            seen[nums[i]] = i