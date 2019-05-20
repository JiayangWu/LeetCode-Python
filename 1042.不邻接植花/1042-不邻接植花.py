class Solution(object):
    def gardenNoAdj(self, N, paths):
        """
        :type N: int
        :type paths: List[List[int]]
        :rtype: List[int]
        """
        from collections import defaultdict
        dic = defaultdict(list)
        
        for path in paths:
            x0, y0 =  path[0], path[1]
            dic[x0].append(y0)
            dic[y0].append(x0)
            
        # print dic
        res = [-1 for _ in range(N + 1)]
        # print len(dic.keys())
        for i in dic.keys():
            neibors = dic[i]
            used = [0 for _ in range(5)]
            
            for neibor in neibors:
                if res[neibor] != -1:
                    used[res[neibor]] = 1
                    
            if sum(used) == 0:
                res[i] = 1
            else:
                for j in range(1, 5):
                    if used[j] == 0:
                        res[i] = j
                        break
        # print res
        for i, x in enumerate(res):
            if x == -1:
                res[i] = 1
        return res[1:]
            
        