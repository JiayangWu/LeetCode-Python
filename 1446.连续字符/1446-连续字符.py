class Solution(object):
    def maxPower(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 1
        pre = s[0]
        tmp = 1
        for i, ch in enumerate(s):
            if i:
                if ch == pre:
                    tmp += 1
                else:
                    pre = ch
                    tmp = 1
                res = max(res, tmp)
        return res