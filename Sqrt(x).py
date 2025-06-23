class Solution:
    def mySqrt(self, x: int) -> int:
        low, high, res = 0, x, 0
        while low <= high:
            mid = (low + high) // 2
            if (mid * mid) < x:
                low = mid + 1
                res = mid
            elif (mid * mid) > x:
                high = mid - 1
            else:
                return mid
        return res
            
