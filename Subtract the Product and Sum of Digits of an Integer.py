class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        digits = str(abs(n))
        total = sum(int(d) for d in digits)
        product = math.prod(int(d) for d in digits)
        return product - total
