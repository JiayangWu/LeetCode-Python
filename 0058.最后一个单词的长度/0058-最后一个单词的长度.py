class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) <= 0 :
            return 0
        s = s.rstrip(" ")
        print s,s.split(" ")
        return len(s.split(" ")[-1])
        