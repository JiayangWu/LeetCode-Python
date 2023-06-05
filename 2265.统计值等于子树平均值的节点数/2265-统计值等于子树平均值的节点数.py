# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:

        self.res = 0
        def getAverageOfSubtree(node):
            # post-order traversal
            # return sum count
            if not node:
                return 0, 0

            left_subtree_sum, left_count = getAverageOfSubtree(node.left)
            right_subtree_sum, right_count = getAverageOfSubtree(node.right)

            subtree_sum = node.val + left_subtree_sum + right_subtree_sum
            subtree_count = left_count + right_count + 1
            if node.val == subtree_sum // subtree_count:
                self.res += 1
            
            return subtree_sum, subtree_count
        
        getAverageOfSubtree(root)
        return self.res