class Solution(object):
    def freqAlphabets(self, s):
        """
        :type s: str
        :rtype: str
        """
        res, i = "", 0
        while i < len(s):
            if i + 2 < len(s) and s[i + 2] == "#":
                res += chr(ord("a") + int(s[i:i + 2]) - 1)
                i += 3
            else:
                res += chr(ord("a") + int(s[i]) - 1)
                i += 1
        return res