# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return root 
        new_root = TreeNode(-1)

        cur, stack = root, []
        parent = None
        while cur or stack:
            if cur:
                stack.append(cur)
                cur = cur.left 
            else:
                cur = stack.pop()
                cur.left = None
                if not parent:
                    parent = cur
                    new_root.right = parent 
                else:
                    parent.right = cur 
                    parent = cur   
                cur = cur.right 
        return new_root.right
