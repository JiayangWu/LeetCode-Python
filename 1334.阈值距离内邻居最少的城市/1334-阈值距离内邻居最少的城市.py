class Solution(object):
    def findTheCity(self, n, edges, distanceThreshold):
        """
        :type n: int
        :type edges: List[List[int]]
        :type distanceThreshold: int
        :rtype: int
        """
        distance = [[float("inf") for j in range(n)] for i in range(n)]
            
        for start, end, w in edges:
            distance[start][end] = w
            distance[end][start] = w
        for i in range(n):
            distance[i][i] = 0
        for i in range(n):
            for j in range(n):
                for k in range(n):
                     distance[j][k] = min(distance[j][k], distance[j][i] + distance[i][k])

        min_cnt = 101
        res = None
        for i in range(n):
            cnt = 0
            for j in range(n):
                if distance[i][j] <= distanceThreshold:
                    cnt += 1

            if cnt <= min_cnt:
                res = i
                min_cnt = cnt
        return res
        