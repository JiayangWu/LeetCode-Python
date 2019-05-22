# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        next_layer = [root]
        result = [root.val]
        while(next_layer):
            temp_next_layer = []
            for node in next_layer:
                if not node:
                    continue
                if node.left:
                    temp_next_layer.append(node.left)
                if node.right:
                    temp_next_layer.append(node.right)
            # print temp_next_layer[0].val
            if temp_next_layer:
                next_layer = temp_next_layer
                result.append(temp_next_layer[-1].val)
                # print result
            else:
                break
            
        return result
                