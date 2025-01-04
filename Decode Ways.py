class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s or s[0] == '0':
            return 0
            
        # dp[i] represents ways to decode string up to index i
        dp = [0] * (len(s) + 1)
        dp[0] = 1  # empty string has 1 way
        dp[1] = 1  # first char has 1 way if not '0'
        
        for i in range(2, len(s) + 1):
            # Check one digit (if not zero)
            if s[i-1] != '0':
                dp[i] += dp[i-1]
                
            # Check two digits (10-26)
            two_digit = int(s[i-2:i])
            if 10 <= two_digit <= 26:
                dp[i] += dp[i-2]
        
        return dp[len(s)]
