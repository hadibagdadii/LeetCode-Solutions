class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        iterate thru each char in s
        lowercase and letters only
        append to test string
        check if reverse test string equals test string
        """
        letters_only = ''.join(char for char in s if (char.isalpha() or char.isnumeric()))
        lowercase_s = letters_only.lower()
        reversed_lowercase_s = ''.join(reversed(lowercase_s))
        if lowercase_s == reversed_lowercase_s:
            return True
        return False
        
