class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        return 1 + (num - 1) % 9 if num > 9 else num