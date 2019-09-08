class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        res = ""
        while n:
            n -= 1
            char = chr(ord('A') + n % 26)
            n /= 26
            res += char
        return res[::-1]