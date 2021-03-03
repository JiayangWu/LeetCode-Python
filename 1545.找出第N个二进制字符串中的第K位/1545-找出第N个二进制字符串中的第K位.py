class Solution(object):
    def findKthBit(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        # len 1， 3， 7， 15 ... L(n) = 2 * (L(n - 1)) + 1
        # if k == 2 * (n - 2) + 2: return 1
        s = "0"
        while len(s) <= k:
            s = s + "1" + "".join([str(1 - int(ch)) for ch in s])[::-1]
            # print (s)
        return s[k - 1]