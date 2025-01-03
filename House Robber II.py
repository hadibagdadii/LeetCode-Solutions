class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        total = []
        total.append(nums[0])
        for n in range(1, len(nums)-1):
            if n == 1:
                total.append(max(nums[0],nums[1]))
            else:
                total.append(max(nums[n] + total[n-2], total[n-1]))
        max1 = total[len(nums)-2]

        total = []
        total.append(nums[1])
        for n in range(2, len(nums)):
            if n == 2:
                total.append(max(nums[1],nums[2]))
            else:
                total.append(max(nums[n] + total[n-3], total[n-2]))
        max2 = total[len(nums)-2]

        return max(max1, max2)
