class Solution(object):
    def canConvertString(self, s, t, k):
        """
        :type s: str
        :type t: str
        :type k: int
        :rtype: bool
        """
        from collections import defaultdict

        if not s or not t or len(s) != len(t):
            return False

        d = list()

        for i in range(len(s)):
            if s[i] < t[i]:
                d.append(ord(t[i]) - ord(s[i]))
            elif s[i] > t[i]:
                d.append(26 - ord(s[i]) + ord(t[i]))

        d.sort()
        res = 0
        pre = None
        for distance in d:
            if not pre or pre != distance:
                res = max(res, distance)
                pre = distance
                pre_cnt = 1
            else:
                res = max(res, 26 * pre_cnt + distance)
                pre_cnt += 1
            if res > k:
                return False
        return True

