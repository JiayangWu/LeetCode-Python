class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        if len(str1) < len(str2):
            str1, str2 = str2, str1 

        for i in range(len(str2), 0, -1):

            if len(str1) % i == 0 and str2[:i] * (len(str1) / i) == str1 and len(str2) % i == 0 and str2[:i] * (len(str2) / i) == str2:
                return str2[:i]
        return ""