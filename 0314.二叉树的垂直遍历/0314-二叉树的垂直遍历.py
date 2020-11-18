# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return None

        from collections import defaultdict, deque

        queue = deque([(0, root)])
        res = defaultdict(list) # key is column idx in the result, value is all elements that have that idx
        while queue: 
            col_idx, node = queue.popleft()

            res[col_idx].append(node.val)

            if node.left:
                queue.append((col_idx - 1, node.left))
            if node.right:
                queue.append((col_idx + 1, node.right))

        return [val for idx, val, in sorted(res.items(), key=lambda x: x[0])]
            
