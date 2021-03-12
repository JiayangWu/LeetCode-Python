class Solution(object):
    def modifyString(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = []
        for i, ch in enumerate(s):
            if ch == "?":
                for new in "abc":
                    if ((i and res[-1] != new) or not i) and ((i < len(s) - 1 and s[i + 1] != new) or i == len(s) - 1):
                        res.append(new)
                        break
            else:
                res.append(ch)

        return "".join(res)