class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        longest = 0
        l = 0
        counts = [0] * 26
    
        for r in range(len(s)):
            counts[ord(s[r]) - 65] += 1
            window_len = r - l + 1
            most_freq = max(counts)
            
            if window_len - most_freq > k:
                counts[ord(s[l]) - 65] -= 1
                l += 1
            
            longest = max(longest, r - l + 1)
        
        return longest
