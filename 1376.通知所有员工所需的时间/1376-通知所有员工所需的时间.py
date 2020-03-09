class Solution(object):
    def numOfMinutes(self, n, headID, manager, informTime):
        """
        :type n: int
        :type headID: int
        :type manager: List[int]
        :type informTime: List[int]
        :rtype: int
        """
        from collections import defaultdict, deque
        layer = defaultdict(set)
 
        for i in range(n):
            layer[manager[i]].add(i) # key is the boss, val is the sub
            
        self.res = 0
        
        def dfs(hid, time):
            if hid not in layer:
                self.res = max(self.res, time)
                return
            
            for sub in layer[hid]:
                dfs(sub, time + informTime[hid])
                
        dfs(headID, 0)
        return self.res
                
                