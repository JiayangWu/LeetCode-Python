# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def constructFromPrePost(self, pre, post):
        """
        :type pre: List[int]
        :type post: List[int]
        :rtype: TreeNode
        """
        
        l1, l2 = len(pre), len(post)
        if l1 == 0 or l2 == 0:
            return 
        
        root = TreeNode(pre[0])
        if l1 == 1:
            return root
        
        pos = post.index(pre[1]) #pos代表左子树的元素在post里最右出现的位置
        len_left = pos + 1
        
        pre_left = pre[1:len_left + 1]
        post_left = post[:pos + 1]
        
        pre_right = pre[len_left +1:]
        post_right = post[pos + 1: -1]
        
        # print pre_left, post_left
        # print pre_right, post_right
        root.left = self.constructFromPrePost(pre_left, post_left)
        root.right = self.constructFromPrePost(pre_right, post_right)
        
        return root
                
        
        