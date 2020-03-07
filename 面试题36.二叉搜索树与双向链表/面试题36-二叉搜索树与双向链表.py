"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""
class Solution(object):
    def treeToDoublyList(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return root 
        if not root.left and not root.right:
            root.left = root 
            root.right = root 
            return root 
        
        left = self.treeToDoublyList(root.left)
        right = self.treeToDoublyList(root.right)
        if root.left and root.right:
            left_tail = left.left 
            right_tail = right.left 

            left_tail.right = root 
            root.left = left_tail 
            root.right = right 
            right.left = root 

            left.left = right_tail 
            right_tail.right = left 
        elif root.left:
            left_tail = left.left 
            left_tail.right = root 
            root.left = left_tail 
            left.left = root 
            root.right = left 
        elif root.right:
            right_tail = right.left 
            root.right = right 
            root.left = right_tail 
            right_tail.right = root 
            right.left = root
        return left if left else root