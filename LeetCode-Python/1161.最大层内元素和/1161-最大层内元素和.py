# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        queue = [root]
        max_level_sum = float("-inf")
        max_level_sum_id = 0
        cur_level_id = 0

        while queue:
            next_queue = []
            cur_level_sum = 0
            cur_level_id += 1
            for node in queue:
                if node:
                    cur_level_sum += node.val
                    if node.left:
                        next_queue.append(node.left)
                    if node.right:
                        next_queue.append(node.right)
            
            if cur_level_sum > max_level_sum:
                max_level_sum = cur_level_sum
                max_level_sum_id = cur_level_id

            queue = next_queue

        return max_level_sum_id