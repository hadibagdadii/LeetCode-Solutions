# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 1, n  # Versions are 1 to n
        
        while left < right:  # Note: left < right, not left <= right
            mid = (left + right) // 2
            
            if isBadVersion(mid):
                right = mid  # First bad version is at mid or before
            else:
                left = mid + 1  # First bad version is after mid
        
        return left  # left == right, pointing to first bad version
