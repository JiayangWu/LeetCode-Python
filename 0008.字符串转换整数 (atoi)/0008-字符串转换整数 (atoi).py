class Solution(object):
    def myAtoi(self, s):
        """
        :type str: str
        :rtype: int
        """
        s = s.strip(" ")
        if not len(s): #排除空
            return 0
        if s[0] not in ["+", "-"] and not s[0].isdigit(): #排除第一个非空字符不是数字
            return 0
        op = 1
        res = ""
        for i, char in enumerate(s):
            if i == 0 :
                if char == "-":
                    op = -1
                    continue
                elif char == "+":
                    continue
            if char == " " or not char.isdigit():
                break
            res += char
        # print res, op
        if len(res) > 0:
            res = op * int(res)
        else:
            return 0
        INT_MIN = -2 **31
        INT_MAX = 2 **31 - 1
        if res > INT_MAX:
            return INT_MAX
        elif res < INT_MIN:
            return INT_MIN
        return res
        