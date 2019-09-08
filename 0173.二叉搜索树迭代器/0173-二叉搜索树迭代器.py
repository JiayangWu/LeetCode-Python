# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        
        def inorder(node):
            if not node:
                return []
            return inorder(node.left) + [node.val] + inorder(node.right)
        self.l = inorder(root)
        self.idx = 0
    def next(self):
        """
        @return the next smallest number
        :rtype: int
        """
        self.idx += 1
        return self.l[self.idx - 1]

    def hasNext(self):
        """
        @return whether we have a next smallest number
        :rtype: bool
        """
        return self.idx < len(self.l)


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()