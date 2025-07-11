class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        seen = set()
        duplicate = -1
        
        # Find duplicate
        for num in nums:
            if num in seen:
                duplicate = num
            seen.add(num)
        
        # Find missing
        n = len(nums)
        expected_sum = n * (n + 1) // 2
        actual_sum = sum(nums)
        missing = expected_sum - actual_sum + duplicate
        
        return [duplicate, missing]
