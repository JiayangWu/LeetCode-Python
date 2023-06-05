# Definition for Node.
# class Node:
#     def __init__(self, val=0, left=None, right=None, random=None):
#         self.val = val
#         self.left = left
#         self.right = right
#         self.random = random

from collections import deque
class Solution:
    def copyRandomBinaryTree(self, root: 'Optional[Node]') -> 'Optional[NodeCopy]':
        if not root:
            return root

        old2new = dict()
        queue = deque([root])
        while queue:
            cur_node = queue.popleft()
            new_node = NodeCopy(cur_node.val)
            old2new[cur_node] = new_node

            if cur_node.left:
                queue.append(cur_node.left)
            if cur_node.right:
                queue.append(cur_node.right)

        queue = deque([root])
        while queue:
            cur_node = queue.popleft()
            new_node = old2new[cur_node]

            if cur_node.left:
                new_node.left = old2new[cur_node.left]
                queue.append(cur_node.left)
            if cur_node.right:
                new_node.right = old2new[cur_node.right]
                queue.append(cur_node.right)
            if cur_node.random:
                new_node.random = old2new[cur_node.random]

        return old2new[root]