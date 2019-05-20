class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        n, flag = divmod(n, 2)
        while(n):
            n, t = divmod(n, 2)
            
            if t == flag:
                return False            
            flag = t
            
        return True