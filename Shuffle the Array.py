class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        midpoint = len(nums) // 2
        result = []
        for i in range(midpoint):
            result.append(nums[i])
            result.append(nums[i + midpoint])
        return result
