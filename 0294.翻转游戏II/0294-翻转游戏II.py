class Solution(object):
    def canWin(self, string):
        """
        :type s: str
        :rtype: bool
        """
        record = {}
        def helper(s):
            if s in record:
                return record[s]
            for i in range(len(s) - 1):
                if s[i:i + 2] == "++":
                    next_s = s[:i] + "--" + s[i + 2:]
                    if not helper(next_s):
                        record[next_s] = False
                        return True
            return False # ++²»´æÔÚ
        
        return helper(string)