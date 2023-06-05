class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        P = [i for i in range(1, m + 1)]
        res = []
        for query in queries:
            index = P.index(query)
            res.append(index)
            P = [P[index]] + P[:index] + P[index + 1:]
        return res