from heapq import *
class DoubleHeap(object):
    def __init__(self):
        self.maxh = []
        self.minh = []
        heapify(self.maxh)
        heapify(self.minh)
        
    def insert(self, val):
        heappush(self.minh, val)
        heappush(self.maxh, -heappop(self.minh))
        if len(self.maxh) > len(self.minh):
            heappush(self.minh, -heappop(self.maxh))
            
    def findMedian(self):
        if len(self.maxh) == len(self.minh):
            return (self.minh[0] - self.maxh[0]) / 2.0
        return self.minh[0]/1.0


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        dh = DoubleHeap()
        for num in nums1:
            dh.insert(num)
            
        for num in nums2:
            dh.insert(num)
            
        return dh.findMedian()