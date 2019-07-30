class Solution(object):
    def removeVowels(self, S):
        """
        :type S: str
        :rtype: str
        """
        
        return "".join(char for char in S if char not in "aeiou")