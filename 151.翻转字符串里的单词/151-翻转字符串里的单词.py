class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return " ".join([item for item in s.strip().rstrip().split(" ") if item][::-1])