class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        res = ["" for _ in indices]
        for i in range(len(s)):
            res[indices[i]] = s[i] 
        return "".join(ch for ch in res)