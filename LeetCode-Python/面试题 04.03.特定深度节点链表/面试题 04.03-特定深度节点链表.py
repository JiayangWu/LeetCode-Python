# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def listOfDepth(self, tree: TreeNode) -> List[ListNode]:
        queue = [tree]
        res = []

        while queue:
            next_queue = []
            cur_level = ListNode(-1)
            p = cur_level
            for node in queue:
                if node:
                    next_queue.extend([node.left, node.right])
                    p.next = ListNode(node.val)
                    p = p.next

            if cur_level != p:
                res.append(cur_level.next)
            queue = next_queue
        return res