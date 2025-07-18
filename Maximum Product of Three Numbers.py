class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        return max(nums[-1] * nums[-2] * nums[-3], nums[0] * nums[1] * nums[-1])

'''
more efficient

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        max1 = max2 = max3 = float('-inf')
        min1 = min2 = float('inf')
        
        for num in nums:
            # Update maximums
            if num > max1:
                max3, max2, max1 = max2, max1, num
            elif num > max2:
                max3, max2 = max2, num
            elif num > max3:
                max3 = num
            
            # Update minimums
            if num < min1:
                min2, min1 = min1, num
            elif num < min2:
                min2 = num
        
        return max(max1 * max2 * max3, min1 * min2 * max1)
'''
