class Solution:
    def reverseWords(self, s: str) -> str:
        output = ""
        words_array = s.split()
        reversed_words_array = words_array[::-1]
        for word in reversed_words_array:
            output = output + word + " "
        output = output.rstrip()
        return output
