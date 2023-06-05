class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        from collections import defaultdict
        src2des = defaultdict(set)

        res = 0
        visited = set()
        for edge in edges:
            src, des = edge[0], edge[1]
            src2des[src].add(des)
            src2des[src].add(src)
            src2des[des].add(src)
            src2des[des].add(des)

        for node in range(n):
            if node not in visited:
                connected = True
                visited.add(node)
                for connected_node in src2des[node]:
                    visited.add(connected_node)
                    if src2des[connected_node] != src2des[node]:
                        connected = False
                        break
                    
                if connected:
                    res += 1
        return res