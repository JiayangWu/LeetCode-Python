class Solution(object):
    def minJumps(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        from collections import defaultdict, deque
        dic = defaultdict(list)
        for i, x in enumerate(arr):
            if (i and arr[i] != arr[i - 1]) or (i < len(arr) - 1 and arr[i] != arr[i + 1]):
                dic[x].append(i)

        queue = deque([(0, 0)]) #pos, step 
        visited = set([0])

        while queue:
            pos, step = queue.popleft() 

            if pos == len(arr) - 1:
                return step

            for p in [pos - 1, pos + 1] + dic[arr[pos]]:
                if 0 <= p < len(arr) and p not in visited:
                    queue.append((p, step + 1))
                    visited.add(p)
