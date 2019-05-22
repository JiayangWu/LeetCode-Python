class Solution(object):
    def isPalindrome(self, x):

        s = str(x)
        if len(s) <= 1:
            return True
        print len(s) / 2
        for count in range(0, len(s)/2):
            if s[count] != s[len(s)-1  - count]:
                return False
        return True