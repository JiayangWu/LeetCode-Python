class Solution(object):
    def removeOuterParentheses(self, S):
        """
        :type S: str
        :rtype: str
        """
        s = list()
        l,r = 0, 0
        res = ""
        for i, x in enumerate(S):
            if x == "(":
                s.append(x)
                l += 1
            elif x == ")":
                r += 1
                if l == r:         
                    print s[1:]
                    res += "".join(s[1:]) #s[0]和新来的x= ")"刚好构成最外层的"()"，所以不要它们就好啦       
                    s = list()
                else:
                    s.append(x)
     
        return res
                