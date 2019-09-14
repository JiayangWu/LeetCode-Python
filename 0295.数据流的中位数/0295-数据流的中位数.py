from heapq import *
# class Heaps(object):
#     def __init__(self):
#         self.min_heap = []
#         self.max_heap = []
        
#     def __
class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min_heap = []
        self.max_heap = []
        heapify(self.min_heap)
        heapify(self.max_heap)

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        heappush(self.min_heap, num)
        heappush(self.max_heap, -heappop(self.min_heap))
        if len(self.max_heap) > len(self.min_heap):
            heappush(self.min_heap, -heappop(self.max_heap))
        

    def findMedian(self):
        """
        :rtype: float
        """
        l_min_heap = len(self.min_heap)
        l_max_heap = len(self.max_heap)
        if l_min_heap == l_max_heap:
            return (self.min_heap[0] - self.max_heap[0]) /2.
        else:
            return self.min_heap[0]/1.
            
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()