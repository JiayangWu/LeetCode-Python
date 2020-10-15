# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""
        
        s = ""
        def preorder(node):
            if not node:
                return "#"

            return str(node.val) + "," + preorder(node.left) + "," +preorder(node.right)
        s = preorder(root)
        return s

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data or data == "#":
            return None
        queue = deque(data.split(","))
        return self.helper(queue)

    def helper(self, queue):
        cur = queue.popleft()
        if cur == "#":
            return None
        root = TreeNode(cur)
        root.left = self.helper(queue)
        root.right = self.helper(queue)

        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))