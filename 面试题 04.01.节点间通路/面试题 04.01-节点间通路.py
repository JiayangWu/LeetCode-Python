from collections import *
class Solution:
    def findWhetherExistsPath(self, n: int, graph: List[List[int]], start: int, target: int) -> bool:
        src2des = defaultdict(list)

        for pair in graph:
            src, des = pair[0], pair[1]
            src2des[src].append(des)

        # BFS 
        queue = deque([start])
        visited = {start}
        while queue:
            cur = queue.popleft()
            if cur == target:
                return True

            for node in src2des[cur]:
                if node not in visited:
                    queue.append(node)
                    visited.add(node)

        return False

            


