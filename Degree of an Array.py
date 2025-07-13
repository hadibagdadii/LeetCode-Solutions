class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        # Track count, first occurrence, and last occurrence of each number
        count = {}
        first = {}
        last = {}
        
        for i, num in enumerate(nums):
            if num not in count:
                count[num] = 0
                first[num] = i
            count[num] += 1
            last[num] = i
        
        # Find the degree (maximum frequency)
        degree = max(count.values())
        
        # Find shortest subarray among all numbers with max frequency
        min_length = len(nums)
        for num in count:
            if count[num] == degree:
                length = last[num] - first[num] + 1
                min_length = min(min_length, length)
        
        return min_length
