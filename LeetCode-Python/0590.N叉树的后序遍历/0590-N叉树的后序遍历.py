"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        # left, right, root => root, right, left
        if not root:
            return []
        res = []
        stack = [root]

        while stack:
            cur = stack.pop()
            if isinstance(cur, Node):
                stack.append(cur.val)
                for child in cur.children[::-1]:
                    stack.append(child)
            else:
                res.append(cur)
        return res