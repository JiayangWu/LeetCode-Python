"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        # root, left, right => right, left, root
        if not root:
            return []
        res = []
        stack = [root]

        while stack:
            cur = stack.pop()
            if isinstance(cur, Node):
                for child in cur.children[::-1]:
                    stack.append(child)
                stack.append(cur.val)
            else:
                res.append(cur)
        return res