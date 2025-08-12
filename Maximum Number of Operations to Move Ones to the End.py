class Solution:
    def maxOperations(self, s: str) -> int:
        operations = 0
        ones_seen = 0
        
        for i in range(len(s) - 1):
            if s[i] == '1':
                ones_seen += 1
            
            # If current is '1' and next is '0', we can perform operation
            if s[i] == '1' and s[i + 1] == '0':
                operations += ones_seen
        
        return operations
