class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        unique_nums = set(nums)
        
        if len(unique_nums) < 3:
            return max(unique_nums)
        
        first = second = third = float('-inf')

        for n in unique_nums:
            if n >= first:
                third = second
                second = first
                first = n
            elif n >= second:
                third = second
                second = n
            elif n >= third:
                third = n
        return third
