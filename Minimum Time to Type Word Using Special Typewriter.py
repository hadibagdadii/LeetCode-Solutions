class Solution:
    def minTimeToType(self, word: str) -> int:
        time = 0
        current = 'a'
        
        for char in word:
            dist = abs(ord(char) - ord(current))
            time += min(dist, 26 - dist) + 1
            current = char
        
        return time
