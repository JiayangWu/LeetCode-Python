class Solution(object):
    def maxDepthAfterSplit(self, seq):
        """
        :type seq: str
        :rtype: List[int]
        """
        # print self.depth("((()))")
        res = [0 for _ in range(len(seq))]
        cnt = 0
        for i, x in enumerate(seq):
            if x == "(":
                cnt += 1
                res[i] = cnt % 2
            else:
                res[i] = cnt % 2
                cnt -= 1
        return res
