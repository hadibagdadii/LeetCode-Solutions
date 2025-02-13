class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        result = []
        keymap = {
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz"
        }

        def backtrack(i, curr):
            if len(curr) == len(digits):
                result.append(curr)
                return
            for char in keymap[digits[i]]:
                backtrack(i + 1, curr + char)

        backtrack(0, "")
        if digits:
            return result
        return []
