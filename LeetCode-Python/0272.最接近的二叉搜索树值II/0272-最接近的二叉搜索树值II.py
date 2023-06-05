# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from  heapq import *
class Solution:
    def closestKValues(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:
        max_heap = []

        def inorder(node):
            if not node:
                return

            inorder(node.left)
            if len(max_heap) < k:
                heappush(max_heap, (-abs(node.val - target), node.val))
            else:
                heappushpop(max_heap, (-abs(node.val -  target), node.val))
            inorder(node.right)
        
        inorder(root)
        return [val for _, val in max_heap]

            