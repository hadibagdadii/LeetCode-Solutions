class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        total = 0
        for sentence in sentences:
            wordCount = sentence.count(' ') + 1
            total = max(total, wordCount)
        return total
