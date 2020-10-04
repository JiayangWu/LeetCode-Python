class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        left, right = 0, 0
        dic = dict()
        res = 0
        while right < len(s):
            if s[right] in dic:
                left = max(left, dic[s[right]] + 1)
            dic[s[right]] = right
            res = max(res, right - left + 1)
            right += 1
        return res