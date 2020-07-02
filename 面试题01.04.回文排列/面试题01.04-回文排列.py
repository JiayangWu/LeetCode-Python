class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        from collections import Counter
        odd_cnt = 0
        for key, val in Counter(s).items():
            if val % 2:
                odd_cnt += 1
                if odd_cnt > 1:
                    return False
        return True