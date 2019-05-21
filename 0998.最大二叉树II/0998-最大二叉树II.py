# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def insertIntoMaxTree(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        A = []
        self.inorder(root, A)
        A.append(val)
        print A
        # A.sort()
        
        return self.constructMaximumBinaryTree(A)
    
    def inorder(self, root, result):
        if not root:
            return
        
        self.inorder(root.left, result)
        result.append(root.val)
        self.inorder(root.right, result)
        return
    
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        root = TreeNode(max(nums))
        root.left = self.constructMaximumBinaryTree(nums[:nums.index(root.val)])
        root.right = self.constructMaximumBinaryTree(nums[nums.index(root.val)+1:])
        return root
        
        