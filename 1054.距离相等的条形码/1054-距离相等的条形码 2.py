class Solution(object):
    def rearrangeBarcodes(self, barcodes):
        """
        :type barcodes: List[int]
        :rtype: List[int]
        """
        from collections import Counter
        import heapq
        
        record = Counter(barcodes) #ͳ��ÿ�����ֳ��ֵ�Ƶ��
        
        queue = []
        for key, val in record.items():
            queue.append([-val, key])
            
        heapq.heapify(queue) #�������ȼ�����

        res = []
        pre = None
        while queue or pre:
            if queue:
                cur = heapq.heappop(queue) #ȡ����ǰ���ִ�������Ԫ�أ����������ͬ���Ƚ��ȳ�
                #frequency, value = cur[0], cur[1]
                res.append(cur[1]) #�����ŵ�����
                cur[0] += 1 #������Ƶ�� - 1����ΪPython֧����С�ѣ�Ϊ�˴ﵽ���ѵ�Ч��������ȡ���෴������
                if cur[0] == 0: #���Ԫ���Ѿ��ź���
                    cur = None
            else:
                cur = None
            if pre: #��ǰһ����������ٽ�����Ѳ���
                heapq.heappush(queue, pre)
            pre = cur #����һ�ֵ�����pre������������ʱ��������ڶ�����Ա�������Ԫ�ز����ظ�
                
        return res
