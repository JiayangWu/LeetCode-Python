# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class FindElements(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        root.val = 0
        self.values = set()
        def dfs(node):
            if not node:
                return 
            self.values.add(node.val)
            if node.left:
                node.left.val = 2 * node.val + 1
                dfs(node.left)
            if node.right:
                node.right.val = 2 * node.val + 2
                dfs(node.right)
        dfs(root)
        
        

    def find(self, target):
        """
        :type target: int
        :rtype: bool
        """
        
        return target in self.values

# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)