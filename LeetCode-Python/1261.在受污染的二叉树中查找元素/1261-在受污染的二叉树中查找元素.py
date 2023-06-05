# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        root.val = 0
        self.values = set()
        def dfs(node):
            if not node:
                return
            
            self.values.add(node.val)
            if node.left:
                node.left.val = 2 * node.val + 1
            if node.right:
                node.right.val = 2 * node.val + 2
            
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)

    def find(self, target: int) -> bool:
        return target in self.values


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)