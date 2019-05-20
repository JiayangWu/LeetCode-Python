class Solution(object):
    def scoreOfParentheses(self, S):
        """
        :type S: str
        :rtype: int
        """
        # ()代表1， ))代表)*2, )(代表+
        s = ""
        
        for i in range(len(S) - 1):
            if S[i] == "(":
                if S[i + 1] == "(":
                    s += "("
                else:
                    s += "1"
                    
            else:
                if S[i + 1] == "(":
                    s += "+"
                else:
                    s += ")*2"
                    
        # print s
        return eval(s)