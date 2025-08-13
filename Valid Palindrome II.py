class Solution:
    def validPalindrome(self, s: str) -> bool:
        def check_palindrome(left, right, can_remove):
            while left < right:
                if s[left] == s[right]:
                    left += 1
                    right -= 1
                elif can_remove:
                    return (check_palindrome(left + 1, right, False) or 
                            check_palindrome(left, right - 1, False))
                else:
                    return False
            return True
        
        return check_palindrome(0, len(s) - 1, True)
