class Solution:
    def longestPalindrome(self, s: str) -> int:
        dictionary = {}
        
        for letter in s:
            dictionary[letter] = dictionary.get(letter, 0) + 1
        
        extra = False
        length = 0
        
        for count in dictionary.values():
            if count % 2 == 1:
                extra = True
            length += (count // 2) * 2
        
        return length + 1 if extra else length
