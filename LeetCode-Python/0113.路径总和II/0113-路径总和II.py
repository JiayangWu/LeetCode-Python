# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
#         self.res = []
#         def dfs(node, path_sum, path):
#             if not node:
#                 return 

#             path_sum += node.val
#             path.append(node.val)
#             if targetSum == path_sum and (not node.left and not node.right):
#                 self.res.append(path[:])
            
#             dfs(node.left, path_sum, path[:])
#             dfs(node.right, path_sum, path[:])
        
#         dfs(root, 0, [])
#         return self.res

from collections import deque
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        
        res = []
        queue = deque([(root, root.val, [root.val])]) # node, cur_path_sum, cur_path

        while queue:
            node, cur_path_sum, cur_path = queue.popleft()
            # print(cur_path_sum, cur_path, not node.left, not node.right)
            if not node.left and not node.right and cur_path_sum == targetSum:
                res.append(cur_path[:])
                continue
            
            if node.left:
                queue.append((node.left, cur_path_sum + node.left.val, cur_path + [node.left.val]))

            if node.right:
                queue.append((node.right, cur_path_sum + node.right.val, cur_path + [node.right.val]))

        return res