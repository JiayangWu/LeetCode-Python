class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        from collections import deque 
        
        queue = deque([(0, 0)])
        visited = set([0])
        while queue:
            cur, step = queue.popleft()
            if cur == amount:
                return step
            if cur > amount:
                continue
            
            for coin in coins:
                value = cur + coin
                if value not in visited:
                    visited.add((value))
                    queue.append((value, step + 1))
            
        return -1