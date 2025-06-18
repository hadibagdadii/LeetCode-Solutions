class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longest = ""
        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    return longest
            longest += s[i]
        return longest
