class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        from collections import Counter
        
        # Count frequency of each task
        count = Counter(tasks)
        max_freq = max(count.values())
        
        # Count how many tasks have the maximum frequency
        max_count = sum(1 for freq in count.values() if freq == max_freq)
        
        # Calculate minimum time using formula
        # (max_freq - 1) * (n + 1) + max_count
        min_time = (max_freq - 1) * (n + 1) + max_count
        
        # Return max of calculated time and total tasks
        return max(min_time, len(tasks))
