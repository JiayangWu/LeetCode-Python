class Solution(object):
    def balancedStringSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        # print s
        l, r = 0, 0
        
        for i in range(len(s)):
            if s[i] == "R":
                r += 1
            else:
                l += 1
            # print r, l
            if l == r:
                return 1 + self.balancedStringSplit(s[i + 1:])
            
        return 0