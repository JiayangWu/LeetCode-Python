class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        l = set()
        while(n!= 1):
            l.add(n)
            temp = 0
            while(n > 0):
                temp += (n % 10) ** 2
                n /= 10
            n = temp
            if n in l:
                return False
                    
        return n == 1