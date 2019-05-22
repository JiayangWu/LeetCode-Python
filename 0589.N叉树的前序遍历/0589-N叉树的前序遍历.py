"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if not root:
            return list()
        result = list()
        result.append(root.val)
        
        for leaf in root.children:
            result += self.preorder(leaf)
            
        return result