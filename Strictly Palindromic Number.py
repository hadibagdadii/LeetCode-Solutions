class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        def to_base(num, base):
            if num == 0:
                return "0"
            digits = []
            while num:
                digits.append(str(num % base))
                num //= base
            return ''.join(reversed(digits))
        
        def is_palindrome(s):
            return s == s[::-1]
        
        # Check if n is palindromic in every base from 2 to n-2
        for base in range(2, n - 1):
            base_representation = to_base(n, base)
            if not is_palindrome(base_representation):
                return False
        
        return True
