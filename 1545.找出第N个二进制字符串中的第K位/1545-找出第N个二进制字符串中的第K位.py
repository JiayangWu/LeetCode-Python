class Solution(object):
    def findKthBit(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """

        def invert(s):
            res = ""
            for ch in s:
                if ch == "0":
                    res += "1"
                else:
                    res += "0"
            return res

        i = 1
        s = "0"
        while i < n:
            s = s + "1" + invert(s)[::-1]
            i += 1
            if k - 1 < len(s):
                return s[k - 1]
        return s[k - 1]
