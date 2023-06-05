# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def nextLargerNodes(self, head):
        """
        :type head: ListNode
        :rtype: List[int]
        """
        h = head
        l = list()
        while(h): #这个循环是为了把链表转数组
            l.append(h.val)
            h = h.next
            
        stack = list()
        res = [0 for i in range(len(l))]
        
        cnt = 0
        while(cnt < len(l)): #从前到后线性扫描
            if not stack or l[stack[-1]] >= l[cnt]: #如果stack为空，或者当前栈顶对应的元素比当前扫描元素还大
                stack.append(cnt)#就直接把当前下标压入栈
            else:#如果当前下标对应的元素比栈顶元素大，就说明找到了比栈顶元素大的下一个数
                while(stack and l[stack[-1]] < l[cnt]): #一直出栈，直到栈顶元素比当前元素小
                    res[stack[-1]] = l[cnt]                    
                    stack.pop()
                stack.append(cnt) #把当前元素压入栈
                
            cnt += 1
            
        return res
        