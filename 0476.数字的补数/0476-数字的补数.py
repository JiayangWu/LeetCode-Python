class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        res = 0
        pos = 0
        while(num >= 2):
            temp = num % 2
            if not temp:
                res += 2 ** pos
            num /= 2
            pos += 1
        return res
        