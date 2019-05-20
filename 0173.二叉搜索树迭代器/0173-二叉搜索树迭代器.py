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
        self.pushLeft(root)

    def next(self):
        """
        @return the next smallest number
        :rtype: int
        """
        popedNode = self.stack.pop()
        self.pushLeft(popedNode.right)
        return popedNode.val

    def hasNext(self):
        """
        @return whether we have a next smallest number
        :rtype: bool
        """
        return len(self.stack) != 0
    
    def pushLeft(self, node):
        while(node):
            self.stack.append(node)
            node = node.left
    


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()