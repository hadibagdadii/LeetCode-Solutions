class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle in haystack:
            position = haystack.find(needle)
            return position
        else:
            return -1
