# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from heapq import *
class Solution(object):
    def closestKValues(self, root, target, k):
        """
        :type root: TreeNode
        :type target: float
        :type k: int
        :rtype: List[int]
        """
        def inOrder(node):
            if not node:
                return []
            return inOrder(node.left) + [node.val] + inOrder(node.right)
        
        l = inOrder(root)
        subs = []
        heapify(subs)
        for num in l:
            sub = abs(target - num)
            heappush(subs, (-sub, num))
            if len(subs) > k:
                heappop(subs)
                
        res = []
        for sub, num in subs:
            res.append(num)
        return res
            