"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""
class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        from collections import defaultdict, deque
        # neibors = defaultdict(list) # key is the original nodes, value is its neibors
        mapping = dict() # key is the original node, value is its copy
        
        queue = deque([node])
        visited = set()
        visited.add(node)
        while queue:
            cur = queue.popleft()
            visited.add(cur)

            copy = Node(cur.val, [])
            mapping[cur] = copy
            for neigh in cur.neighbors:
                if neigh not in visited:
                    queue.append(neigh)
                    
        for cur, copy in mapping.items():
            for each in cur.neighbors:
                copy.neighbors.append(mapping[each])
        return mapping[node]