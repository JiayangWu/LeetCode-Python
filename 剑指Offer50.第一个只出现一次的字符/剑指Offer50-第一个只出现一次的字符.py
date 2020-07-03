class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: str
        """
        from collections import Counter
        dic = Counter(s)
        
        for ch in s:
            if dic[ch] == 1:
                return ch
        return " "