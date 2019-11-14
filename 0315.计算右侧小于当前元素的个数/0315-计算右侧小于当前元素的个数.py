class TreeNode(object):
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val
        self.left_subtree_cnt = 0
        
class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        # 从左往右处理，右边是未知的，所以不好弄
        # 从右往左处理，则对于每个数，其右边的数都已知
        res = [0 for _ in nums]
        root = None
        for i, num in enumerate(nums[::-1]):
            root = self.insert(root, num, i, res)
        return res[::-1]
    
    def insert(self, root, val, i, res):
        if not root:
            root = TreeNode(val)
        elif root.val >= val:
            root.left_subtree_cnt += 1
            root.left = self.insert(root.left, val, i, res)
        elif root.val < val:
            res[i] += root.left_subtree_cnt + 1
            root.right = self.insert(root.right, val, i, res)
            
        return root
            
            