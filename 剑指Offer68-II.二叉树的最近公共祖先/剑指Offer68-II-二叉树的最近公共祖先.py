# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        child2par = {root: None}
        stack = [root]
        
        while stack:
            cur = stack.pop()
            if cur.left:
                stack.append(cur.left)
                child2par[cur.left] = cur
            if cur.right:
                stack.append(cur.right)
                child2par[cur.right] = cur

        p_ancestors = set()
        while p in child2par:
            p_ancestors.add(p)
            p = child2par[p]
        
        res = root
        while q in child2par:
            if q in p_ancestors:
                return q
            q = child2par[q]
        return res
