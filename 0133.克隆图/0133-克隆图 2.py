class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        from collections import defaultdict, deque
        neighborList = defaultdict(list) #�����ϣ�����ڼ�¼�Ͻ������ھӵĹ�ϵ, key��ÿ���Ͻ�㣬val������neighbors
        mapping = dict() #�����ϣ�����ڼ�¼�Ͻ�������Ӧ���½ڵ�
        
        def bfs(queue):
            if not queue:
                return
            newqueue = deque()
            
            while queue:
                cur = queue.popleft()
                mapping[cur] = Node(cur.val, []) #Ϊÿ���Ͻ�㴴��һ����Ӧ���½ڵ�
                for nei in cur.neighbors:
                    neighborList[cur].append(nei) #��¼�µ�ǰ�Ͻ��������ھ�
                    if nei not in visited:
                        visited.add(nei)
                        newqueue.append(nei)
            bfs(newqueue) #BFS����һ��
         
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
                        if not neighborList[node]: #���û���ھ�
                            return

                        for nei in neighborList[node]: #����ÿ���ھ�
                            mapping[node].neighbors.append(mapping[nei]) #���µĽ���ǡ��Ͻ����ھӶ�Ӧ�ġ��½��
                            if nei not in visited:
                                visited.add(nei)
                                newqueue.append(nei)
                queue = newqueue[:]

        generate([node])

        return mapping[node] #�����������Ӧ���½ڵ�