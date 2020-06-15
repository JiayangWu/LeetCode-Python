class Solution(object):
    def checkIfCanBreak(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        s1 = sorted(s1)
        s2 = sorted(s2)
        
        return all(s1[i] >= s2[i] for i in range(len(s1))) or all(s2[i] >= s1[i] for i in range(len(s1)))