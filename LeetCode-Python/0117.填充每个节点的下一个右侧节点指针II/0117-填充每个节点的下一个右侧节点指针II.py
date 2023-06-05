"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root

        def findCousin(node, parent):
            parent_nxt = parent.next
            while parent_nxt:
                if parent_nxt.left:
                    node.next = parent_nxt.left
                    return
                
                if parent_nxt.right:
                    node.next = parent_nxt.right
                    return
                
                parent_nxt = parent_nxt.next
            
        def dfs(node):
            if not node:
                return node

            if node.right and node.left:
                node.left.next = node.right
                findCousin(node.right, node)
            elif node.left:
                findCousin(node.left, node)
            elif node.right:
                findCousin(node.right, node)

            dfs(node.right)
            dfs(node.left)
            

        dfs(root)
        return root