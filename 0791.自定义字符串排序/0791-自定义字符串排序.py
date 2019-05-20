class Solution(object):
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        res = ""
        
        for char in S:
            res += char * T.count(char)
            
        for char in T:
            if char not in S:
                res += char
        
        return res