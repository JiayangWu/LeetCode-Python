class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        s = bin(num)[2:]
        b = ""
        for ch in s:

            if ch == "0":
                b += "1"
            else:
                b += "0"
        # print b
        return int(b,2)