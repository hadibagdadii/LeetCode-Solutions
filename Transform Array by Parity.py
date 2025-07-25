class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        count = 0
        for n in nums:
            if n % 2 == 0:
                count += 1
        for x in range(count):
            nums[x] = 0
        for x in range(count, len(nums)):
            nums[x] = 1
        return nums
