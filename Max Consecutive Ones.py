class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = res = 0
        for n in nums:
            count = 0 if n == 0 else count + 1
            res = max(count, res)
        return res
