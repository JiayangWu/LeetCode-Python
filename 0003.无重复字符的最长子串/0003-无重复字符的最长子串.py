class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        record = {}
        start, res = 0, 0
        for end in range(len(s)):
            if s[end] in record:
                start = max(start, record[s[end]] + 1)
                
            record[s[end]] = end
            res = max(res, end - start + 1)
            
        return res