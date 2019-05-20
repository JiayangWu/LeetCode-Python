class Solution(object):
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #贪心+trierTree
        root = TreeNode(-1)
        
        for num in nums:
            cur_node = root #当前的node
            
            for i in range(0, 32):               #代表32个位
                # print num, 1 <<(31 - i), num & (1 <<(31 - i))
                if num & (1 <<(31 - i)) == 0:    #如果当前位与运算的结果是1， 就往左走
                    if not cur_node.left:
                        cur_node.left = TreeNode(0)
                    cur_node = cur_node.left
                else:                            #如果当前位与运算的结果是0， 就往右走
                    if not cur_node.right:
                        cur_node.right = TreeNode(1)
                    cur_node = cur_node.right
            cur_node.left = TreeNode(num)        #在最后的左叶子节点记录一下这个数的值
                    
        res = 0
        for num in nums:
            cur_node = root
            
            for i in range(0, 32):
                # print cur_node.val, cur_node.left, cur_node.right
                if num & (1 <<(31 - i)) == 0:     #与运算结果为0，如果能往右走，就往右走，因为右子树代表1，这样在这一位上异或会得到1
                    if cur_node.right:           #能往右走
                        cur_node = cur_node.right#就往右走
                    else:                        #不能往右走
                        cur_node = cur_node.left#就往左走
                else:                            #与运算结果为1，如果能往左走，就往左走，因为左子树代表0，这样异或会得到1
                    if cur_node.left:            #能往左走
                        cur_node = cur_node.left#就往左走
                    else:                        #不能往左走
                        cur_node = cur_node.right#就往右走  
            temp = cur_node.left.val             #得到这条路径存放的数的值
                
            res = max(res, num ^ temp)           #每次刷新res为最大值
                
        return res