class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        seen = {}
        res = []
        for n in nums1:
            if n in seen:
                seen[n] += 1
            else:
                seen[n] = 1
        for n in nums2:
            if n in seen and seen[n] > 0:
                res.append(n)
                seen[n] -= 1
        return res
