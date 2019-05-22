class Solution(object):

    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 1:
            return 1
        if n == 2:
            return 2
        a = 1
        b = 2
        count = 3
        while count<=n:
          c = a + b
          a = b
          b = c
          count += 1
        return c
          
    
