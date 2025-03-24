class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        started = False
        count = 0
        for l in reversed(s):
            if l != ' ' and started == False:
                started = True
                count += 1
            elif l == " " and started == False:
                continue
            elif l != ' ':
                count += 1
            elif l == ' ':
                return count
        return count
            
