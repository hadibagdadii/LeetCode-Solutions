class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        table = {}

        for letter in s:
            if letter in table:
                table[letter] += 1
            else:
                table[letter] = 1

        for letter in t:
            if letter not in table:
                return letter
            elif table[letter] == 0:
                return letter
            else:
                table[letter] -= 1

        # More elegant solution
        # result = 0
        
        # # XOR all characters in both strings
        # for char in s:
        #     result ^= ord(char)
        
        # for char in t:
        #     result ^= ord(char)
        
        # return chr(result)
