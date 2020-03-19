class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        return len(s) -max(0,sum([s.count(i)%2 for i in set(s)])-1)