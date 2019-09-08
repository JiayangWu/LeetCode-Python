class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        multi = dividend * divisor
        op = 1
        if multi == 0:
            return 0
        elif multi <0:
            op = -1
        dividend, divisor = abs(dividend), abs(divisor)
        multi = 1
        res = 0
        while(dividend >= divisor):
            tmp = multi * divisor
            if dividend >= tmp:
                dividend -= tmp
                res += multi
                multi += 1
            else:
                multi = 1
                
        res = res * op
        return res if -2 ** 31 <= res <= 2 ** 31 - 1 else 2 ** 31 - 1