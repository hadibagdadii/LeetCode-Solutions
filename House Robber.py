class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        [2,3,9,1]
        """
        totals = []
        totals.append(nums[0])
        for n in range(1, len(nums)):
            if n == 1:
                totals.append(max(nums[0],nums[1]))
            else:
                totals.append(max(nums[n] + totals[n-2], totals[n-1]))
        return totals[len(nums)-1]

        # to optimize space, reduce to 2 vars
