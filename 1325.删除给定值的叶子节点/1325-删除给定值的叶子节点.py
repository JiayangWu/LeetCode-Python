# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def removeLeafNodes(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: TreeNode
        """
        if not root:
            return root
        root.left = self.removeLeafNodes(root.left, target)
        root.right = self.removeLeafNodes(root.right, target)
        if not root.left and not root.right and root.val == target:
            return None
        return root        
        
#         from collections import defaultdict, deque
#         if not root:
#             return root
#         outdegree = dict()
#         parent = dict()
        
#         # 层序遍历预处理
#         queue = deque([root])
#         while queue:
#             for _ in range(len(queue)):
#                 cur = queue.popleft()
#                 outdegree[cur] = 0
#                 if cur.left:
#                     outdegree[cur] += 1
#                     parent[cur.left] = cur
#                     queue.append(cur.left)
#                 if cur.right:
#                     outdegree[cur] += 1
#                     parent[cur.right] = cur
#                     queue.append(cur.right)
                    
#         queue = deque([])
#         for key, val in outdegree.items():
#             if not val and key.val == target:
#                 queue.append(key)
        
#         while queue:
#             cur = queue.popleft()
#             if cur not in parent:
#                 return None
#             par = parent[cur]
#             if par.left and par.left == cur:
#                 par.left = None
#                 outdegree[par] -= 1
#             if par.right and par.right == cur:
#                 par.right = None
#                 outdegree[par] -= 1
            
#             if outdegree[par] == 0 and par.val == target:
#                 queue.append(par)
                
#         return root
                
        
                
                