class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if not root:
            return 
        def helper(node, val):
            if node.val < val:
                if not node.right:
                    node.right = TreeNode(val)
                else:
                    helper(node.right, val)
            elif node.val > val:
                if not node.left:
                    node.left = TreeNode(val)
                else:
                    helper(node.left, val)
        helper(root, val)
        return root