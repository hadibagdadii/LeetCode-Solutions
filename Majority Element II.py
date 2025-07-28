class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        from collections import Counter
        
        n = len(nums)
        threshold = n // 3
        count = Counter(nums)
        
        result = []
        for num, freq in count.items():
            if freq > threshold:
                result.append(num)
        
        return result
