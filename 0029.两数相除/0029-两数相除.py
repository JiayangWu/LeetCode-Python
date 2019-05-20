class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        # 计算被除数可以减去多少个除数：
        op = 1
        if (dividend > 0 and divisor < 0) or (dividend < 0 and divisor > 0):
            op = -1
        
        dividend, divisor = abs(dividend), abs(divisor)
        res = 0
        while(dividend >= divisor):
            multidivisor, multi = divisor, 1
            while(dividend >= multidivisor):
                res += multi
                dividend -= multidivisor
                multi = multi << 1
                multidivisor = multidivisor <<1
                
            
        INT_MIN = -(2 **31)
        INT_MAX = 2 **31 - 1
        res *= op
        
        return res if INT_MIN <= res <= INT_MAX else INT_MAX 