# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        from collections import defaultdict, deque
        outdegree = defaultdict(int)
        child2parent = {root:None}
        leavesNodes = []
        def dfs(node):
            if not node:
                return
            
            if node.left:
                outdegree[node] += 1
                child2parent[node.left] = node
                dfs(node.left)
            if node.right:
                outdegree[node] += 1
                child2parent[node.right] = node
                dfs(node.right)
            
            if not outdegree[node]:
                leavesNodes.append(node)
        dfs(root)
        
        res = []
        queue = deque(leavesNodes)
        while queue:
            tmp = []
            for _ in range(len(queue)):
                cur = queue.popleft()
                tmp.append(cur.val)
                
                parent = child2parent[cur]
                outdegree[parent] -= 1
                
                if not outdegree[parent]:
                    queue.append(parent)
            res.append(tmp)
        return res
                