# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
          return []
        if not root.left and not root.right:
          return [str(root.val)]
        self.res = []
        def dfs(node, tmp):
          if not node:
            return 
          if not node.left and not node.right:
            self.res.append(tmp + "->" + str(node.val))
          dfs(node.left, tmp + "->" + str(node.val))
          dfs(node.right, tmp + "->" + str(node.val))
          
        dfs(root.left, str(root.val))
        dfs(root.right, str(root.val))
        return self.res