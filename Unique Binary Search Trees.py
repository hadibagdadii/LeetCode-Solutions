class Solution:
    def numTrees(self, n: int) -> int:
        # dp[i] = number of unique BSTs with i nodes
        dp = [0] * (n + 1)
        
        # Base cases
        dp[0] = 1  # Empty tree
        dp[1] = 1  # Single node tree
        
        # Fill dp table
        for i in range(2, n + 1):
            for j in range(1, i + 1):
                # j is the root, left subtree has j-1 nodes, right has i-j nodes
                dp[i] += dp[j - 1] * dp[i - j]
        
        return dp[n]
