"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        result = []
        if not root:
            return 0
        for node in root.children:
            result.append(self.maxDepth(node))
        
        return 1 + max(result) if result else 1