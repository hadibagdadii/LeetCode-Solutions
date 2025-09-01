class Solution:
    def reverse(self, x: int) -> int:
        lower, upper = pow(-2, 31), pow(2, 31) - 1
        if x >= 0:
            digits = int(''.join(reversed(str(x))))
        else:
            digits = int(''.join(reversed(str(abs(x))))) * -1

        if digits >= lower and digits <= upper:
            return digits
        else:
            return 0
