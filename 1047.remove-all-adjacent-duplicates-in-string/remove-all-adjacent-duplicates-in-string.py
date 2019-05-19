class Solution(object):
    def removeDuplicates(self, S):
        """
        :type S: str
        :rtype: str
        """
        flag = 1
        while 1:
            original_l = len(S)
            i = 0
            while i < len(S) - 1:
                if i >= 0 and S[i] == S[i + 1]:
                    S = S[:i] + S[i + 2:]
                    i -= 2
                i += 1 
            if original_l == len(S):
                return S