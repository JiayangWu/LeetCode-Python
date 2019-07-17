# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def numComponents(self, head, G):
        """
        :type head: ListNode
        :type G: List[int]
        :rtype: int
        """
        g = []
        G = set(G)
        p = head
        while p: #处理相对排序
            if p.val in G:
                g.append(p.val)
            p = p.next
            
        p, i, res = head, 0, 0
        seperate = True #用于标记当前是不是断开
        while i < len(g) and p:
            if g[i] == p.val:
                if seperate == True: #当前是断开状态
                    res += 1 #所以给res + 1
                    seperate = False #表示当前是连续
                p = p.next
                i += 1
            else:
                seperate = True #已经断开
                p = p.next
        return res
        
   