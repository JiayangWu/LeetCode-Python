class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        
        
        res = list()
        ls, lp = len(s), len(p)        
        if lp > ls:
            return list()
        
        lo, hi = 0, lp - 1
        s1 = [0 for _ in range(26)]
        s2 = [0 for _ in range(26)]
        
        for i in range(lp):
            s2[ord(p[i]) - 97] += 1
            
        for i in range(lp - 1):
            s1[ord(s[i]) - 97] += 1
        
        for i in range(ls - lp + 1):
            s1[ord(s[i + lp - 1]) - 97] += 1
            
            if s1 == s2:
                res.append(i)
            
            s1[ord(s[i]) - 97] -= 1
        
        return res