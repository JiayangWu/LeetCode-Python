# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        if not root:
            return []
        next_layer = [root.left, root.right]
        result = [float(root.val)]
        
        while(next_layer):
            temp_next_layer = list()
            layer_value = list()
            for node in next_layer:
                if not node:
                    continue
                temp_next_layer.append(node.left)
                temp_next_layer.append(node.right)
                layer_value.append(node.val)
            if layer_value:
                result.append(sum(layer_value) / float(len(layer_value)))
            next_layer = temp_next_layer
        return result
        