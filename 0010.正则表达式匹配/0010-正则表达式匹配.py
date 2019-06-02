class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if not p: #如果p为空，s不空，return false， s空, return true
            return not s
        
        match = s and p[0] in [s[0], "."]
        if len(p) > 1 and p[1] == "*":
            return self.isMatch(s, p[2:]) or (match and self.isMatch(s[1:], p))
        return match and self.isMatch(s[1:], p[1:])