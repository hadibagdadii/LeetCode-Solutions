from collections import Counter

class Solution:
    def maxFreqSum(self, s: str) -> int:
        counter = Counter(s)
        vowels = set('aeiou')
        
        max_vowel_freq = 0
        max_consonant_freq = 0
        
        for char, freq in counter.items():
            if char in vowels:
                max_vowel_freq = max(max_vowel_freq, freq)
            else:
                max_consonant_freq = max(max_consonant_freq, freq)
        
        return max_vowel_freq + max_consonant_freq
