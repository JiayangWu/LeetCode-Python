class Solution(object):
    def minSteps(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        n = len(t)
        from collections import Counter
        dic1 = Counter(s)
        dic2 = Counter(t)
        
        valid = 0
        for char, fre in dic2.items():
            valid += min(dic1[char], fre)
            
        return n - valid