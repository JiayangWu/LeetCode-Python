class Solution(object):
    def countLetters(self, S):
        """
        :type S: str
        :rtype: int
        """
        res = 0
        for i in range(len(S)):
            for j in range(i + 1, len(S) + 1):
                substring = S[i:j]
                if substring == substring[0] * len(substring):
                    res += 1
                    # print substring
        return res