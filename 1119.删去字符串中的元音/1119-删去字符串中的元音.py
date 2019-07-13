class Solution(object):
    def removeVowels(self, S):
        """
        :type S: str
        :rtype: str
        """
        res = ""
        for char in S:
            if char not in "aeiou":
                res += char
                
        return res