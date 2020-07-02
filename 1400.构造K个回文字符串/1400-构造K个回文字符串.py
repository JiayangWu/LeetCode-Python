class Solution(object):
    def canConstruct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: bool
        """
        if k >= len(s):
            # 长度 == k，必然可以；长度 < k，必然不可以。
            return k == len(s)

        from collections import Counter
        dic = Counter(s) 
        # 对于每一个出现次数为奇数次的字符来说，比如 "aaa", 它至少能构成一个回文串，最多能构成三个回文串，
        s_odd = 0
        for val in dic.values():
            if val % 2:
                s_odd += 1
        return s_odd <= k