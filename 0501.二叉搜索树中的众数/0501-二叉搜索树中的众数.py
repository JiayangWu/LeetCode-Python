# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def inorder(node):
            if not node:
                return []
            return inorder(node.left) + [node.val] + inorder(node.right)
        l = inorder(root)
        
        
        dic = collections.defaultdict(int)
        for i, x in enumerate(l):
            dic[x] += 1
        # print dic
        
        maxf = 1
        res = set()
        for key, val in dic.items():
            if val > maxf:
                res = set()
                res.add(key)
                maxf = val
            if val == maxf:
                res.add(key)
                
        return list(res)
#         self.maxf = 1
#         self.res = []
        
#         def dfs(node, parent, cnt):
#             if not node:
#                 return
#             if node.val == parent:
#                 cnt += 1
#             cnt += dfs(node.left, node.val, cnt) + dfs(node.right, node.val, cnt)
            