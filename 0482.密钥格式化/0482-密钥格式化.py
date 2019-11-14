class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        s = "".join(S.split("-")).upper()
        length_of_first_part = len(s) % K
        if not length_of_first_part:
            length_of_first_part = K
            
        res = s[:length_of_first_part]
        for i in range(length_of_first_part, len(s), K):
            res += "-"
            res += s[i:i+K]
        return res
        