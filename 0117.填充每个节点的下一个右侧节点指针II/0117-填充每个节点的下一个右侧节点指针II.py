class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root or (not root.left and not root.right):
            return root
        
        def findCousin(node, parent):
            tmp = parent.next
            while(tmp):
                if tmp.left:
                    node.next = tmp.left
                    break
                    
                elif tmp.right:
                    node.next = tmp.right
                    break
                tmp = tmp.next
                
        if root.left and root.right:
            root.left.next = root.right
            findCousin(root.right, root)
            
        elif root.left:
            findCousin(root.left, root)
            
        elif root.right:
            findCousin(root.right, root)
        
        # print root.val, root.right.next
        self.connect(root.right)
        self.connect(root.left)
        
                
        return root