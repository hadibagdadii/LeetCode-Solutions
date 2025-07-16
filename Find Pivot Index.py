class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        leftsum = 0
        
        for i in range(len(nums)):
            rightsum = total_sum - leftsum - nums[i]
            if leftsum == rightsum:
                return i
            leftsum += nums[i]
        
        return -1
