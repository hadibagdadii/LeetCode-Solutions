class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total, maxi = 0, 0
        for n in nums:
            total += n
            if total > maxi:
                maxi = total
            if total <= 0:
                total = 0
        if total == 0 and maxi == 0:
            return max(nums)
        return maxi
