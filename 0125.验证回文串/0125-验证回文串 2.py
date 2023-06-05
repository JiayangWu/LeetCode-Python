class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        tmp = ""
        for char in s.lower():
            if char.isalpha() or char.isdigit():
                tmp += char
        print tmp
        return tmp == tmp[::-1]