class Solution(object):
    def longestPrefix(self, s):
        """
        :type s: str
        :rtype: str
        """
        base = 131
        mod = 10 ** 9 + 7
        res = ""
        prefix, suffix = 0, 0
        multiple = 1
        for i in range(len(s) - 1):
            prefix = (prefix * base + ord(s[i])) % mod 
            suffix = (ord(s[-(i + 1)]) * multiple + suffix) % mod 
            if prefix == suffix:
                res = s[:i + 1]
            
            multiple = multiple * base % mod

        return res