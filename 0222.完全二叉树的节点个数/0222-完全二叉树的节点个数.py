# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        self.leavesCnt = 0
        self.height = 0
        self.flag = 0
        def dfs(node, layer):
            if not node or self.flag:
                return
            if not node.left and not node.right:
                
                self.height = max(self.height, layer)
                if layer < self.height:
                    self.flag = 1
                else:
                    self.leavesCnt += 1
                return 
            dfs(node.left, layer + 1)
            dfs(node.right, layer + 1)
            
        dfs(root, 0)
        # print self.leavesCnt
        return self.leavesCnt + sum([2 ** i for i in range(self.height)] )