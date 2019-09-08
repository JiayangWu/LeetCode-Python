class Solution(object):
    def myAtoi(self, s):
        """
        :type str: str
        :rtype: int
        """
        s = s.strip(" ")
        # print s
        if not s or (s[0] not in ["+", "-"] and not s[0].isdigit()):
            return 0
        
        op = 1
        tmp = ""
        for i, char in enumerate(s):
            if i == 0:
                if char == "-":
                    op = -1
                    continue
                elif char == "+":
                    pass
                    continue       
            if char.isdigit():
                tmp += char
            else:
                break
        # print tmp
        if tmp:
            res = op * int(tmp)
        else:
            res = 0
        INT_MAX = 2 **31 - 1
        INT_MIN = -2 **31
        if res > INT_MAX:
            return INT_MAX
        elif res < INT_MIN:
            return INT_MIN
        else:
            return res