class Solution(object):
    def thousandSeparator(self, n):
        """
        :type n: int
        :rtype: str
        """
        res = ""
        cnt = 0
        for digit in str(n)[::-1]:
            res += digit
            cnt += 1
            if cnt == 3:
                cnt = 0
                res += "."

        return res[::-1].strip(".")