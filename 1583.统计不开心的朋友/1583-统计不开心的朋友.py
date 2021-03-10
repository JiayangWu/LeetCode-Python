class Solution(object):
    def unhappyFriends(self, n, preferences, pairs):
        """
        :type n: int
        :type preferences: List[List[int]]
        :type pairs: List[List[int]]
        :rtype: int
        """
        # 建立亲密度矩阵，prefer_degrees[i][j]即为 i 对 j 的亲密度
        prefer_degrees = [[-n-1 for _ in range(n)] for _ in range(n)]
        for i, preference in enumerate(preferences):
            for degree, j in enumerate(preference):
                prefer_degrees[i][j] = -degree

        # 建立配对字典，给定x， ppl2friends[x]即为 x 分配的朋友
        ppl2friends = dict()
        for x, y in pairs:
            ppl2friends[x] = y
            ppl2friends[y] = x

        def isUnhappy(x):
            # 判定 x 是否快乐
            y = ppl2friends[x]

            for u in range(n):
                v = ppl2friends[u]
                if x != u and prefer_degrees[x][u] > prefer_degrees[x][y] and \
                   prefer_degrees[u][x] > prefer_degrees[u][v]:
                   return 1
            return 0

        return sum([isUnhappy(i) for i in range(n)])