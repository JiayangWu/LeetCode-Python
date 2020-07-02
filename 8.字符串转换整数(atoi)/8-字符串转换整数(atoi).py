class Solution(object):
    def myAtoi(self, s):
        """
        :type str: str
        :rtype: int
        """
        s = s.strip()
        
        if not s:
            return 0
        
        sign = 1
        INT_MAX, INT_MIN = 2 ** 31 - 1, -(2 ** 31)

        if s[0] == "+":
            s = s[1:]
        elif s[0] == "-":
            s = s[1:]
            sign = -1
        elif not s[0].isdigit():
            return 0
        
        num = "0"
        for ch in s:
            if ch.isdigit():
                num += ch
            else:
                break
        
        num = sign * int(num)
        
        if num > INT_MAX:
            return INT_MAX
        elif num < INT_MIN:
            return INT_MIN
        return num