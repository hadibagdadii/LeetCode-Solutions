class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curr_max, curr_min, ans = nums[0], nums[0], nums[0]
        for n in range(1, len(nums)):
            if nums[n] < 0:
                curr_max, curr_min = curr_min, curr_max
            curr_max = max(nums[n], curr_max * nums[n])
            curr_min = min(nums[n], curr_min * nums[n])
            ans = max(ans, curr_max)

        return ans
