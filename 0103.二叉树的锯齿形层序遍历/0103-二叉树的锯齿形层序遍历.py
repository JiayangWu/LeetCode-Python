# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = [root]
        res = []
        flag = 1
        while queue:
            next_queue = []
            cur_level = []
            for node in queue:
                if node:
                    next_queue.extend([node.left, node.right])
                    cur_level.append(node.val)

            if cur_level:
                if flag:
                    res.append(cur_level)
                    flag = 0
                else:
                    flag = 1
                    res.append(cur_level[::-1])
            queue = next_queue
        return res