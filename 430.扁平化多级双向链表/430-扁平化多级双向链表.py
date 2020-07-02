"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""
class Solution(object):
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return head

        def helper(node):
            # 返回的是最后一个节点
            if not node:
                return 
            while node:
                nxt = node.next # 备份 next
                if not nxt:
                    tail = node # 记录 tail，用于返回
                if node.child:
                    node.next = node.child # 把child 变成next
                    node.next.prev = node 
                    t = helper(node.child) # 递归处理，t 是处理之后的 原来的child 的最后一个节点
                    node.child = None # 把child 置空
                    if nxt: # 如果有next 部分，就让next的prev指向 原来的child 处理之后的最后一个节点
                        nxt.prev = t
                    t.next = nxt # 让 t.next 指向原来的 next
                node = node.next
            return tail
        helper(head)
        return head