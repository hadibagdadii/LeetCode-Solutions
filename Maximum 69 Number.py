class Solution:
    def maximum69Number (self, num: int) -> int:
        digits = [int(digit) for digit in str(num)]
        for index, value in enumerate(digits):
            if value == 6:
                digits[index] = 9
                break
        return int(''.join(map(str, digits)))
