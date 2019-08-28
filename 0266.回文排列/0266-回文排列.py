class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        flag = 0
        dic = collections.Counter(s)
        
        for key, val in dic.items():
            if val % 2:
                if not flag:
                    flag = 1
                else:
                    return False
        
        return True