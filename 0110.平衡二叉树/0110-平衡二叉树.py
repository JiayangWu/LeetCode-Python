class Solution(object):
    def isBalanced(self, root):
        if not root:
            return True
        
        def check(root,height):
            if not root:
                return True,height
            
            tag1,height1=check(root.left,height+1)
            tag2,height2=check(root.right,height+1)
            if tag1 and tag2 and abs(height1-height2)<2:
                return True,max(height1,height2)
            else:
                return False,height1
            
        tag,height=check(root,0)
        return tag  