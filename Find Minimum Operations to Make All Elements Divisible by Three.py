class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        total = 0
        for n in nums:
            if n % 3 != 0:
                total += 1
        return total
