class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        my_dict = {}
        for letter in magazine:
            if letter in my_dict:
                my_dict[letter] = my_dict[letter] + 1
            else:
                my_dict[letter] = 1

        for letter in ransomNote:
            if letter in my_dict:
                if my_dict[letter] == 0:
                    return False
                else:
                    my_dict[letter] = my_dict[letter] - 1
            else:
                return False
        return True
