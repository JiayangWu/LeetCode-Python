# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        queue = [root]
        lor = 0 # 0 for left and 1 for right
        res = list()
        if not root:
            return []
        while(queue):
            next_queue = list()
            layer = list()
            
            for node in queue:
                if node.left:
                    next_queue.append(node.left)
                if node.right:
                    next_queue.append(node.right)
                
                layer.append(node.val)

            if not lor: # left
                res.append(layer)
            else:
                res.append(layer[::-1])
            
            lor = 1 - lor
            queue = next_queue
        return res