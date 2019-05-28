from collections import deque
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        record = []
        for i in range(1, int(n ** 0.5) + 1):
            record.append(i * i)
        # print record
        visited = set()
        q = deque()
        q.append([0, 0])
        while(q):
            m, cnt = q.popleft()
            
            for num in record:
                s = m + num
                if s == n:
                    return cnt + 1
                if s < n and s not in visited:
                    visited.add(s)
                    q.append([s, cnt + 1])
        # return
                    
            
        
        