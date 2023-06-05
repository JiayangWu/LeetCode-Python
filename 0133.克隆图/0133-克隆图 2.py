class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        from collections import defaultdict, deque
        neighborList = defaultdict(list) #这个哈希表用于记录老结点和其邻居的关系, key是每个老结点，val是它的neighbors
        mapping = dict() #这个哈希表用于记录老结点和它对应的新节点
        
        def bfs(queue):
            if not queue:
                return
            newqueue = deque()
            
            while queue:
                cur = queue.popleft()
                mapping[cur] = Node(cur.val, []) #为每个老结点创建一个对应的新节点
                for nei in cur.neighbors:
                    neighborList[cur].append(nei) #记录下当前老结点的所有邻居
                    if nei not in visited:
                        visited.add(nei)
                        newqueue.append(nei)
            bfs(newqueue) #BFS找下一层
         
        visited = {node}           
        q = deque()
        q.append(node)
        bfs(q)
        visited = {node}
        
        def generate(queue):
            while queue:
                newqueue = []
                for node in queue:
                    if node:                
                        if not neighborList[node]: #如果没有邻居
                            return

                        for nei in neighborList[node]: #处理每个邻居
                            mapping[node].neighbors.append(mapping[nei]) #在新的结点标记【老结点的邻居对应的】新结点
                            if nei not in visited:
                                visited.add(nei)
                                newqueue.append(nei)
                queue = newqueue[:]

        generate([node])

        return mapping[node] #返回输入结点对应的新节点