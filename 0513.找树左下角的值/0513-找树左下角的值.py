# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        next_layer = [root]
        while(next_layer):
            temp_next_layer = []
            layer_value = []
            for node in next_layer:
                if node.left:                    
                    temp_next_layer.append(node.left)
                if node.right:
                    temp_next_layer.append(node.right)
                layer_value.append(node.val)
                # print layer_value 
            next_layer = temp_next_layer
            
        # print layer_value        
        return layer_value[0]