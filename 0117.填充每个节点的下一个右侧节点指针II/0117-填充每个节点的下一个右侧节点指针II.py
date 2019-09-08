"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, left, right, next):
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
            return
        wait = None
        if root.left and root.right:
            root.left.next = root.right
            wait = root.right
        elif root.left:
            wait = root.left
        elif root.right:
            wait = root.right
        else:
            return root
        p = root.next
        while p:
            if p.left:
                wait.next = p.left
                break
            elif p.right:
                wait.next = p.right
                break
            else:
                p = p.next

       
        self.connect(root.right)
        self.connect(root.left)
        return root 