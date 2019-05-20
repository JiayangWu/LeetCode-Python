# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def recoverFromPreorder(self, S):
        """
        :type S: str
        :rtype: TreeNode
        """
 
        def helper(string, cnt):  
            lr = string[string.find(cnt * "-") + 1:].strip("-") #lr代表包含左子树和右子树的字符串

            if len(lr) == 0:
                return None

            scnt = string.count("-")

            if scnt == 0:
                # print "no left children and no right children", string
                return TreeNode(int(string))
            
            node = TreeNode(string[:string.find(cnt * "-")])
            
            c = 0
            pos = -1
            
            for i in range(len(lr)):
                if lr[i] == "-":
                    c += 1
                else:
                    if c == cnt:
                        pos = i
                        break
                    c = 0
                    
            if pos == -1: #没找到cnt * "-"，说明只有left
                node.left = helper(lr, cnt + 1)
                node.right = None
            else:
                l = lr[:pos - cnt]
                r = lr[pos:]
                # print "leftpart is", l
                # print "rightpart is", r  
                node.right = helper(r, cnt + 1)
                node.left  = helper(l, cnt + 1)
            
            return node

        return helper(S, 1)
            
            