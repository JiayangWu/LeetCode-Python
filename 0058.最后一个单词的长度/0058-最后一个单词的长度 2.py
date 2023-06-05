class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        cnt = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] != " ":
                while i >= 0 and s[i] != " ":
                    cnt += 1
                    i -= 1
                break
        return cnt