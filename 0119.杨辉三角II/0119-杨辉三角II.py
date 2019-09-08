class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if not rowIndex:
            return [1]
        res = [[1]]
        for i in range(1, rowIndex + 1):
            tmp = [1]
            for j in range(1, i):
                tmp.append(res[j - 1] + res[j])
            tmp.append(1)
            res = tmp[:]
        return res     