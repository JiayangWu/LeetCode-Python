"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if not root:
            return []
        from collections import deque 
        queue = deque([root])
        res = []
        while queue:
            layer = []
            for _ in range(len(queue)):
                cur = queue.popleft() 
                if cur:
                    layer.append(cur.val)
                    for child in cur.children:
                        queue.append(child)
            res.append(layer)
        
        return res
