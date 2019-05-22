"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if not root:
            return []
        nodes = [root]
        node_val = list(list())
        self.generate(nodes, node_val)
        return node_val
    
    def generate(self, nodes, node_val):
        new_node = []
        new_node_val = []
        for node in nodes:
            for leaf in node.children:
                new_node.append(leaf)
            new_node_val.append(node.val)
        node_val.append(new_node_val)
        if len(new_node) == 0:
            return
        self.generate(new_node, node_val)
        