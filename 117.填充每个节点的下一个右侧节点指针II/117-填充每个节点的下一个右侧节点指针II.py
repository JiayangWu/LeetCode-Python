"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return root
        
        if root.left and root.right:
            root.left.next = root.right
            root.right.next = self.findNext(root)
        
        elif root.left:
            root.left.next = self.findNext(root)
        elif root.right:
            root.right.next = self.findNext(root)
            
        self.connect(root.right)
        self.connect(root.left)
        
        return root
    
    def findNext(self, node):
        nxt = node.next
        while nxt:
            if nxt.left:
                return nxt.left
            if nxt.right:
                return nxt.right
            nxt = nxt.next
        return None