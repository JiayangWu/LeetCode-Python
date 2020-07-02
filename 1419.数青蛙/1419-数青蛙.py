class Solution(object):
    def minNumberOfFrogs(self, croakOfFrogs):
        """
        :type croakOfFrogs: str
        :rtype: int
        """
        from collections import defaultdict
        if len(croakOfFrogs) % 5 != 0:
            return -1
        
        dic = defaultdict(int)
        res = 0
        pre = {"r":"c", "o":"r", "a":"o"}
        for ch in croakOfFrogs:
            if ch == "c":
                dic[ch] += 1
            
            elif ch in "roa":
                if dic[pre[ch]] == 0:
                    return -1
                dic[pre[ch]] -= 1
                dic[ch] += 1
                
            elif ch == "k":
                if dic["a"] == 0:
                    return -1
                dic["k"] -= 1
                
            res = max(res, sum(dic.values()))
            
        return res