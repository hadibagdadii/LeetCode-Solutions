class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        index, prev = 0, -101
        while index < len(nums):
            if nums[index] == prev:
                nums.pop(index)
            else:
                prev = nums[index]
                index += 1
        return len(nums)
