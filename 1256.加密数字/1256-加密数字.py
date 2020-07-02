class Solution(object):
    def encode(self, num):
        """
        :type num: int
        :rtype: str
        """
        return bin(num + 1)[3:]