class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <=1 :
            return False
        import math
        s = 1
        for i in range(2, int(math.sqrt(num) + 1)):
            if num % i == 0:
                s += i + num / i
        print s
        
        return s == num