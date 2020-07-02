class Solution(object):
    def canReach(self, arr, start):
        """
        :type arr: List[int]
        :type start: int
        :rtype: bool
        """
        from collections import deque
        queue = deque([start])
        visited = set([start])
        while queue:
            cur = queue.popleft()
            
            if arr[cur] == 0:
                return True 
            
            for i in [cur + arr[cur], cur - arr[cur]]:
                if 0 <= i < len(arr) and i not in visited:
                    visited.add(i)
                    queue.append(i)
        return False