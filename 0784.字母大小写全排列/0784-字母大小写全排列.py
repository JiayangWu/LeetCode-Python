class Solution(object):
    def letterCasePermutation(self, S):
        l = len(S)
        n = 2 ** l
        res = list()
        if l == 0:
            res.append("")
        for i in range(0, n):
            temp = ""

            for j in range(0, l):
                if ((2 ** j) &i) == 0:
                    temp += S[j].lower()
                else:
                    temp += S[j].upper()
            if temp not in res:
                res.append(temp)
        return res
