class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums)
        count_map = {}
        
        # Create mapping of number to count of smaller numbers
        for i, num in enumerate(sorted_nums):
            if num not in count_map:
                count_map[num] = i
        
        # Build result using the mapping
        return [count_map[num] for num in nums]
