class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        sub = {}
        start, longest = 0, 0

        for end, letter in enumerate(s):
            if letter in sub and sub[letter] >= start:
                start = sub[letter] + 1
            sub[letter] = end
            longest = max(longest, end - start + 1)
        return longest
