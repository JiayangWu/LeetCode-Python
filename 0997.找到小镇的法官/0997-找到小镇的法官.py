class Solution(object):
    def findJudge(self, N, trust):
        """
        :type N: int
        :type trust: List[List[int]]
        :rtype: int
        """
        indegree = [0] * (N + 1)
        outdegree = [0] * (N + 1)
        
        res = list()
        
        for pair in trust:
            outdegree[pair[0]] += 1
            indegree[pair[1]] += 1
        
        for i in range(1, N + 1):
            if outdegree[i] == 0 and indegree[i] == N - 1:
                res.append(i)
        
        return res[0] if len(res) == 1 else -1