class Solution(object):
    def largeGroupPositions(self, S):
        """
        :type S: str
        :rtype: List[List[int]]
        """
        start, end = 0, 0
        res = []
        i = 0
        while i < len(S) - 1:
            if S[i] == S[i + 1]:
                start = i
                end = i
            while(end < len(S) - 1 and S[end] == S[end + 1]):
                end += 1
            if end - start + 1 >= 3:
                res.append([start, end])
                i = end + 1
                start = end + 1
                continue
            i += 1
        return res