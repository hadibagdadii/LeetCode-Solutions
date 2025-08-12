class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result = 0
        multiplier = 1
        
        for char in reversed(columnTitle):
            digit_value = ord(char) - ord('A') + 1
            result += digit_value * multiplier
            multiplier *= 26
        
        return result
