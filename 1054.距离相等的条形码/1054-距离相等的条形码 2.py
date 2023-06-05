class Solution(object):
    def rearrangeBarcodes(self, barcodes):
        """
        :type barcodes: List[int]
        :rtype: List[int]
        """
        from collections import Counter
        import heapq
        
        record = Counter(barcodes) #统计每个数字出现的频率
        
        queue = []
        for key, val in record.items():
            queue.append([-val, key])
            
        heapq.heapify(queue) #建立优先级队列

        res = []
        pre = None
        while queue or pre:
            if queue:
                cur = heapq.heappop(queue) #取出当前出现次数最多的元素，如果次数相同则先进先出
                #frequency, value = cur[0], cur[1]
                res.append(cur[1]) #把它放到答案里
                cur[0] += 1 #给它的频率 - 1，因为Python支持最小堆，为了达到最大堆的效果，所以取了相反数操作
                if cur[0] == 0: #这个元素已经放好了
                    cur = None
            else:
                cur = None
            if pre: #把前一个插入的数再进行入堆操作
                heapq.heappush(queue, pre)
            pre = cur #把这一轮的数用pre保存起来，此时这个数不在堆里，可以保障相邻元素不会重复
                
        return res
