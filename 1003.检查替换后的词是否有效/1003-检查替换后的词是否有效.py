class Solution(object):
    def isValid(self, S):
        """
        :type S: str
        :rtype: bool
        """
        l = len(S)
        if l < 3:
            return False
        if S == "abc":
            return True
        if S[0] == "b" or S[0] == "c":
            return False
        if "abc" in S:    
            index = S.index("abc")
        else:
            return False
        # print S
        S = S[: index] + S[index + 3:]
        # print S
        return self.isValid(S)