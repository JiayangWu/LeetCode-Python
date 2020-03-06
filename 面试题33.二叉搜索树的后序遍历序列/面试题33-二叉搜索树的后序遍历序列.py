class Solution(object):
    def verifyPostorder(self, postorder):
        """
        :type postorder: List[int]
        :rtype: bool
        """
        if not postorder or len(postorder) == 1:
            return True
        
        for i in range(len(postorder)):
            if postorder[i] > postorder[-1]:
                break
        if any(postorder[j] < postorder[-1] for j in range(i, len(postorder) - 1)):
            return False
        
        if i == len(postorder):
            # no right subtree
            left = postorder[:-1]
            right = None
        else:
            left = postorder[:i]
            right = postorder[i:-1]
            
        return self.verifyPostorder(left) and self.verifyPostorder(right)
            