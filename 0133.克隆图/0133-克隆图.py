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
        record = defaultdict(list)
        mapping = dict()
        def bfs(queue):
            if not queue:
                return
            newqueue = deque()
            
            while queue:
                cur = queue.popleft()
                mapping[cur] = Node(cur.val, [])
                for nei in cur.neighbors:
                    record[cur].append(nei)
                    if nei not in visited:
                        visited.add(nei)
                        newqueue.append(nei)
            bfs(newqueue)
         
        visited = {node}           
        q = deque()
        q.append(node)
        bfs(q)
        
        # for key, val in record.items():
        #     print key.val
        #     for item in val:
        #         print item.val
        # print mapping
        visited = {node}
        
        def generate(queue):
            while queue:
                newqueue = []
                for node in queue:
                    if node:
                        # print node.val                    
                        if not record[node]: #如果没有邻居
                            return

                        for nei in record[node]: #处理每个邻居
                            mapping[node].neighbors.append(mapping[nei])
                            if nei not in visited:
                                visited.add(nei)
                                newqueue.append(nei)
                queue = newqueue[:]
        q = deque()
        q.append(node)
        generate(q)

        return mapping[node]
                