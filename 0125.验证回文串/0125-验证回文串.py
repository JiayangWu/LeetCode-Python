class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        ss = ""
        for i in s:
            if i.isalpha() != True and i.isdigit() != True:
                print i
                continue
            ss += i
        # print ss
        if len(ss) <= 1:
            return True
        for i in range(0,len(ss)):
            # print ss[i]
            if ss[i] != ss[-i-1]:
                return False
        return True
                
        