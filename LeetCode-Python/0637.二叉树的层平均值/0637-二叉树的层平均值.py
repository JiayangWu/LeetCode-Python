# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        queue = [root]
        res = []

        while queue:
            next_queue = []
            cur_sum = 0
            cur_count = 0

            for node in queue:
                if node:
                    cur_count += 1
                    cur_sum += node.val

                    next_queue.append(node.left)
                    next_queue.append(node.right)
            if cur_count:
                res.append(cur_sum * 1.0 / cur_count)
            queue = next_queue
        return res