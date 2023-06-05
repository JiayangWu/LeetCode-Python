# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        if not root:
            return []
        next_layer = [root]
        result = []
        while(next_layer):
            temp_next_layer = []
            layer_value = []
            for node in next_layer:
                if not node:
                    continue
                layer_value.append(node.val)
                # print layer_value
                if node.left:
                    temp_next_layer.append(node.left)
                if node.right:
                    temp_next_layer.append(node.right)
                
            # print temp_next_layer[0].val
            next_layer = temp_next_layer
            result.append(max(layer_value))

            
        return result
                        