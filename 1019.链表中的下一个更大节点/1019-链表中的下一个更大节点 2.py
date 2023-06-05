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
        while(h): #���ѭ����Ϊ�˰�����ת����
            l.append(h.val)
            h = h.next
            
        stack = list()
        res = [0 for i in range(len(l))]
        
        cnt = 0
        while(cnt < len(l)): #��ǰ��������ɨ��
            if not stack or l[stack[-1]] >= l[cnt]: #���stackΪ�գ����ߵ�ǰջ����Ӧ��Ԫ�رȵ�ǰɨ��Ԫ�ػ���
                stack.append(cnt)#��ֱ�Ӱѵ�ǰ�±�ѹ��ջ
            else:#�����ǰ�±��Ӧ��Ԫ�ر�ջ��Ԫ�ش󣬾�˵���ҵ��˱�ջ��Ԫ�ش����һ����
                while(stack and l[stack[-1]] < l[cnt]): #һֱ��ջ��ֱ��ջ��Ԫ�رȵ�ǰԪ��С
                    res[stack[-1]] = l[cnt]                    
                    stack.pop()
                stack.append(cnt) #�ѵ�ǰԪ��ѹ��ջ
                
            cnt += 1
            
        return res
        