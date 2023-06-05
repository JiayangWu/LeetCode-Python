class Solution:
    def baseNeg2(self, n: int) -> str:
        if not n:
            return "0"
        l = ""
        while n:
            d, m = divmod(n, -2)
            n = - (n // 2)
            l += str(-m)
        return l[::-1]