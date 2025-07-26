class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        
        n = len(nums)
        min_val, max_val = min(nums), max(nums)
        
        if min_val == max_val:
            return 0
        
        bucket_size = max(1, (max_val - min_val) // (n - 1))
        bucket_count = (max_val - min_val) // bucket_size + 1
        
        buckets = [[float('inf'), float('-inf'), False] for _ in range(bucket_count)]
        
        for num in nums:
            bucket_idx = (num - min_val) // bucket_size
            buckets[bucket_idx][0] = min(buckets[bucket_idx][0], num)
            buckets[bucket_idx][1] = max(buckets[bucket_idx][1], num)
            buckets[bucket_idx][2] = True
        
        max_gap = 0
        prev_max = min_val
        
        for bucket in buckets:
            if bucket[2]:
                max_gap = max(max_gap, bucket[0] - prev_max)
                prev_max = bucket[1]
        
        return max_gap
