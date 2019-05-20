class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        record = [0 for i in range(0, 129)]
        for char in s:
            record[ord(char)] += 1
        
        res, flag = 0, 0
        for i, x in enumerate(record):
            if x % 2 == 1:
                res += x - 1
                flag = 1
            else:
                res += x
        # print res        
        return res + flag