class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        even, odd = 0, 1
        
        while even < len(nums) and odd < len(nums):
            # Find misplaced even index
            while even < len(nums) and nums[even] % 2 == 0:
                even += 2
            
            # Find misplaced odd index  
            while odd < len(nums) and nums[odd] % 2 == 1:
                odd += 2
            
            # If both pointers are still valid, swap
            if even < len(nums) and odd < len(nums):
                nums[even], nums[odd] = nums[odd], nums[even]
                
        return nums
