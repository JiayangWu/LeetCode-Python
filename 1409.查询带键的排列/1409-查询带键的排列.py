class Solution(object):
    def processQueries(self, queries, m):
        """
        :type queries: List[int]
        :type m: int
        :rtype: List[int]
        """
        q = list(range(1, m + 1))
        res = []
        for i, x in enumerate(queries):
            idx = q.index(queries[i])
            res.append(idx)
            q.pop(idx)
            q.insert(0, queries[i])
        return res