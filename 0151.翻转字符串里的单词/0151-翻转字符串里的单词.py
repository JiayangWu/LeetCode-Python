class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
            """
        res = []
        s = s.rstrip()
        s = s.lstrip()
        l = s.split(" ")
        l = l[::-1]
        print l
        # print " ".join(item for item in l)    
        # for item in l:
        #     if item == ""
        return " ".join(item for item in l if item != "")