class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        start = 0

        for end in range(len(nums)):
            if nums[end] != val:
                nums[start] = nums[end]
                start += 1
        
        return start
