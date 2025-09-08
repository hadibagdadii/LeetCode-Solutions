class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch in word:
            pos = word.index(ch)
            first = word[:pos+1][::-1]
            return first + word[pos+1:]
        return word
