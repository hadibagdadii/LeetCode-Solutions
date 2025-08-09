class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)  # Convert to list for mutability
        left, right = 0, len(s) - 1
        
        while left < right:
            # Find vowel from left
            while left < right and s[left].lower() not in 'aeiou':
                left += 1
            
            # Find vowel from right
            while left < right and s[right].lower() not in 'aeiou':
                right -= 1
            
            # Swap vowels
            if left < right:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
        
        return ''.join(s)
