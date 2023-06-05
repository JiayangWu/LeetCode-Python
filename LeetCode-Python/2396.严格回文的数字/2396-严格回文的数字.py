class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        for k in range(2, n - 1):
            bk = ""
            temp = n
            while temp:
                temp, m = divmod(temp, k)
                bk += str(m)
            if bk != bk[::-1]:
                return False
        return True