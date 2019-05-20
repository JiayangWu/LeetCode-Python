class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        
        strs.sort()
        res = ""
        
        for x, y in zip(strs[0], strs[-1]):
            if x == y:
                res += x
            else:
                break
        
        return res
                