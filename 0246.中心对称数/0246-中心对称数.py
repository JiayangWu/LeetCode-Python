class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        mapping = {"0":"0", "1":"1", "6":"9","9":"6", "8":"8"}
        newnum = ""
        for i, char in enumerate(num):
            if char not in mapping:
                return False
            newnum += mapping[char]

        return newnum[::-1] == num