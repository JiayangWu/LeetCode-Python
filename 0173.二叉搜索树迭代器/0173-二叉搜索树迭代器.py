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
        self.stack = []
        self.cur = root
        
    def next(self):
        """
        @return the next smallest number
        :rtype: int
        """
        while self.cur or self.stack:
            if self.cur:
                self.stack.append(self.cur)
                self.cur = self.cur.left
            else:
                self.cur = self.stack.pop()
                res = self.cur.val
                self.cur = self.cur.right

                return res
            

    def hasNext(self):
        """
        @return whether we have a next smallest number
        :rtype: bool
        """
        return self.cur or self.stack


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()