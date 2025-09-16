class Solution:
    def defangIPaddr(self, address: str) -> str:
        result = ""
        for digit in address:
            if digit == ".":
                result = result + "[.]"
            else:
                result = result + digit
        return result
