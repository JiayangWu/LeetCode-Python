"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from collections import deque
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node 
        
        old2new = dict()
        queue = deque([node])
        visited = set([node])
        while queue:
            cur_node = queue.popleft()
            new_node = Node(cur_node.val)
            old2new[cur_node] = new_node
            
            for neighbor in cur_node.neighbors:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        
        queue = deque([node])
        visited = set([node])
        while queue:
            cur_node = queue.popleft()
            new_node = old2new[cur_node]
            
            for neighbor in cur_node.neighbors:
                new_neighbor = old2new[neighbor]
                new_node.neighbors.append(new_neighbor)

                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        return old2new[node]

            