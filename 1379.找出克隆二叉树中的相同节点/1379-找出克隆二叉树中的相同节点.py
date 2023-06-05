# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        queue = [cloned]
        while queue:
            next_queue = []
            for node in queue:
                if node:
                    if node.val == target.val:
                        return node
                    next_queue.append(node.left)
                    next_queue.append(node.right)
            queue = next_queue[:]
        