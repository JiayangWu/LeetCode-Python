class Solution(object):
    def sortString(self, s):
        """
        :type s: str
        :rtype: str
        """
        from collections import Counter
        dic = Counter(s)
        res = ""
        while len(res) < len(s):
            for ch in "abcdefghijklmnopqrstuvwxyz":
                if ch in dic and dic[ch]:
                    res += ch 
                    dic[ch] -= 1
            for ch in "abcdefghijklmnopqrstuvwxyz"[::-1]:
                if ch in dic and dic[ch]:
                    res += ch 
                    dic[ch] -= 1

        return res       