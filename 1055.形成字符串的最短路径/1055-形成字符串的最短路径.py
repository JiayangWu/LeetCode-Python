class Solution(object):
    def shortestWay(self, source, target):
        """
        :type source: str
        :type target: str
        :rtype: int
        """
        s = set(source)
        t = set(target)
        for ch in t:
            if ch not in s:
                return -1
            
        i, j = 0, 0
        res = 0
        while j < len(target):
            i = 0
            while i < len(source) and j < len(target):
                if source[i] == target[j]:
                    i += 1
                    j += 1
                else:
                    i += 1
            res += 1
        return res