class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a, b = a[::-1], b[::-1]
        carry, total, res = 0, 0, ""
        for i in range(max(len(a), len(b))):
            bit1 = ord(a[i]) - ord("0") if i < len(a) else 0
            bit2 = ord(b[i]) - ord("0") if i < len(b) else 0

            total = bit1 + bit2 + carry
            res = str(total % 2) + res
            carry = total // 2

        if carry:
            res = "1" + res
        return res
