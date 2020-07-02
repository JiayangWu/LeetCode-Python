class Solution(object):
    def maxScore(self, s):
        """
        :type s: str
        :rtype: int
        """
        zero = s.count("0")
        one = len(s) - zero
        zero_cnt = 0
        res = 0
        for i, x in enumerate(s[:-1]):
            if x == "0":
                zero_cnt += 1
            one_cnt = one - (i + 1 - zero_cnt)
            res = max(res, zero_cnt + one_cnt)

        return res