# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumRootToLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = []
        
        def dfs(root, tmp):
            if not root:
                return
            tmp += str(root.val)
            if not root.left and not root.right:
                res.append(tmp[:])
                
            dfs(root.left, tmp)
            dfs(root.right, tmp)
            tmp = tmp[:-1]
                
        
        
        dfs(root, "")
        # print res
        rres = 0
        for item in res:
            # print item, int(item, 2)
            rres += int(item, 2) 
            rres %= (10 ** 9 + 7)
        
        return rres