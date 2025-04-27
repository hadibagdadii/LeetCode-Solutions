class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        
        if len(pattern) != len(words):
            return False
        
        pattern_to_word = {}
        word_to_pattern = {}
        
        for p, word in zip(pattern, words):
            if p in pattern_to_word and pattern_to_word[p] != word:
                return False
            
            if word in word_to_pattern and word_to_pattern[word] != p:
                return False
            
            pattern_to_word[p] = word
            word_to_pattern[word] = p
        
        return True
