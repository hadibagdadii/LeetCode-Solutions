class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res = []
        nums_set = set(nums)
        for n in range(1, len(nums) + 1):
            if n not in nums_set:
                res.append(n)
        return res
