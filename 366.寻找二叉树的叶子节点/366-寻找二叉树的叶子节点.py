# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        from collections import defaultdict
        self.dic = defaultdict(list)
        res = []
        def get_Height(node):
            if not node:
                return -1
            lh = get_Height(node.left)
            rh = get_Height(node.right)
            h = max(lh, rh) + 1
            self.dic[h].append(node.val)
            return h
        
        get_Height(root)
        # print self.dic
        h = 0
        while 1:
            if h not in self.dic:
                break
            res.append(self.dic[h])
            h += 1
        return res
        