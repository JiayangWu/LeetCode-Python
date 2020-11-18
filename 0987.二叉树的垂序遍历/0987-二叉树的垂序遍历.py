# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def verticalTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        from collections import defaultdict
        dic = defaultdict(list) 
        def dfs(root, x, y): 
            if root:
                dic[x].append((y, root.val))
                dfs(root.left, x - 1, y + 1) 
                dfs(root.right, x + 1, y + 1) 

        dfs(root, 0, 0) 
        res = []
        for k in sorted(dic.keys()): 
            x = [pair[1] for pair in sorted(dic[k])] 
            res.append(x)

        return res