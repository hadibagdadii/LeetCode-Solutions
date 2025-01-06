class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dp = [0] * len(nums)
        dp[-1] = 1
        for index in range(len(nums)-2, -1, -1):
            steps = 0
            while (index + steps) < len(dp) and steps <= nums[index]:
                if dp[index + steps] == 1:
                    dp[index] = 1
                    break
                steps += 1
        print(dp)
        if dp[0] == 1:
            return True
        return False
