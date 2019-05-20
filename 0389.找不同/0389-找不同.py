class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        # return chr(sum(ord(i) for i in list(t)) - sum(ord(j) for j in list(s)))
        # res = 0
#         for i in s:
#             res ^= ord(i) - 97
            
#         for i in t:
#             res ^= ord(i) - 97
        
#         return chr(res + 97)

        alphabet = "abcdefghijklmnopqrstuvwxyz"
    
        for char in alphabet:
            if s.count(char) != t.count(char):
                return char