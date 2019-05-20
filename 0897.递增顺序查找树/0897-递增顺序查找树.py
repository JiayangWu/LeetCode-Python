# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        preorder = list()
        
        def pre_order(root):
            if not root:
                return
            pre_order(root.left)
            preorder.append(root.val)
            pre_order(root.right)
        
        pre_order(root)
        dummy = TreeNode(0)
        for i, node in enumerate(preorder):

            temp = TreeNode(node)
            temp.left = None
            temp.right = None
            if i == 0:
                dummy.right = temp
                cur = temp
            else:
                cur.right = temp
                cur = temp
        return dummy.right