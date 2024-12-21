class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        L = len(nums)
        answer = []

        prefix = 1
        for i in range(L):
            answer.append(prefix) 
            prefix *= nums[i]

        suffix = 1
        for i in reversed(range(L)):
            answer[i] *= suffix
            suffix *= nums[i]

        return answer
