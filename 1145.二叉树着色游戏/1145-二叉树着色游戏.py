# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def btreeGameWinningMove(self, root, n, x):
        """
        :type root: TreeNode
        :type n: int
        :type x: int
        :rtype: bool
        """
        self.x_address = 0
        
        def dfs(node):
            if not node:
                return 
            if node.val == x:
                self.x_address = node
                return
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        
        def cnt_node_in_subtree(node):
            if not node:
                return 0
            return 1 + cnt_node_in_subtree(node.left) + cnt_node_in_subtree(node.right)
        # print root.val
        if root.val == x:     
            return cnt_node_in_subtree(root.left) != cnt_node_in_subtree(root.right)
        else:
            x_cnt = cnt_node_in_subtree(self.x_address)
            total_cnt = cnt_node_in_subtree(root) 
            left_cnt = cnt_node_in_subtree(self.x_address.left)
            right_cnt = cnt_node_in_subtree(self.x_address.right)
            return x_cnt < total_cnt - x_cnt or left_cnt > total_cnt - left_cnt or right_cnt > total_cnt - right_cnt