class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s.strip()
        s = s.rstrip()
        s = s[::-1].split(" ")
        
        return " ".join(item[::-1] for item in s if item)