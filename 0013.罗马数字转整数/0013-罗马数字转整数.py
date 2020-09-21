class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {"I":1, "V": 5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        res = 0
        pre_value = None
        for ch in s:
            if (ch in ["V", "X"] and pre_value == 1) or \
               (ch in ["L", "C"] and pre_value == 10) or \
               (ch in ["D", "M"] and pre_value == 100):
                res += dic[ch] - 2 * pre_value 
            else:
                res += dic[ch]
                pre_value = dic[ch]
        return res
