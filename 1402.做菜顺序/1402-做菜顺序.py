class Solution(object):
    def maxSatisfaction(self, satisfaction):
        """
        :type satisfaction: List[int]
        :rtype: int
        """
        res = 0

        s = sorted(satisfaction)

        for i in range(len(s)):
            cnt = 1
            tmp = 0
            for j in range(i, len(s)):
                tmp += cnt * s[j]
                cnt += 1
            # print tmp
            res = max(tmp, res)

        return res
