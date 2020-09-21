class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        l = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), \
             (100, "C"), (90, "XC"), (50, "L"), (40, "XL"), (10, "X"), \
             (9, "IX"), (5, "V"), (4, "IV"), (1, "I")][::-1]
        res = ""
        while num:
            for value, ch in l[::-1]:
                if num >= value:
                    res += ch 
                    num -= value 
                    break
                else:
                    l.pop()
        return res