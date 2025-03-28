class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0
        
        jumps = 0
        current_max_reach = 0
        next_max_reach = 0
        
        # Don't need to check the last element since we'll always reach it
        for i in range(n - 1):
            # Update the max reachable position from current position
            next_max_reach = max(next_max_reach, i + nums[i])
            
            # If we've come to the end of our current jump range
            if i == current_max_reach:
                # Jump to the furthest position we can reach
                jumps += 1
                current_max_reach = next_max_reach
                
                # If we can already reach the end, break early
                if current_max_reach >= n - 1:
                    break
        
        return jumps
