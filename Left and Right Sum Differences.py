class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        result = []
        left = 0
        right = sum(nums)
        for num in nums:
            right -= num
            result.append(abs(left - right))
            left += num
        return result
