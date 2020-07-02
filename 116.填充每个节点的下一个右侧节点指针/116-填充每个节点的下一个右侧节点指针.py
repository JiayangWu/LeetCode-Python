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
        if not root or not root.left:
            return root

        root.left.next = root.right
        if root.next:
            root.right.next = root.next.left
        self.connect(root.left)
        self.connect(root.right)
        
        return root
    
    def findNext(self, node):
        nxt = node.next
        while nxt:
            if nxt.left:
                return nxt.left
            elif nxt.right:
                return nxt.right
            else:
                nxt = nxt.next
        return None