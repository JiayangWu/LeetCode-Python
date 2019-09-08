class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        tmpp = ""
        for i, char in enumerate(p):
            if p[i] != "*":
                tmpp += p[i]
            else:
                if i == 0 or p[i] != tmpp[-1]:
                    tmpp += "*"
        p = tmpp[:]
        
        memo = {}
        def find(i, j):
            if (i, j) not in memo:
                ans = False
                if j == len(p):
                    ans = i == len(s)
                elif i < len(s):
                    if p[j] in [s[i], "?"]:
                        ans = find(i + 1, j + 1)
                    elif p[j] == "*":
                        ans = find(i, j + 1) or find(i + 1, j)
                elif p[j] == "*":
                    ans = find(i, j + 1)
                memo[i, j] = ans
            return memo[i, j]
        
        return find(0, 0)
                
                    