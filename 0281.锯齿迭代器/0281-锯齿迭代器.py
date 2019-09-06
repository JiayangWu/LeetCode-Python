class ZigzagIterator(object):

    def __init__(self, v1, v2):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        self.i1, self.i2 = 0, 0
        self.v1, self.v2 = v1, v2
        self.indicator = 0 # 0 for v1, 1 for v2

    def next(self):
        """
        :rtype: int
        """
        if not self.indicator:
            self.indicator = 1
            if self.i1 < len(self.v1):
                self.i1 += 1
                return self.v1[self.i1 - 1]
            else:
                self.i2 += 1
                return self.v2[self.i2 - 1]
        else:
            self.indicator = 0
            if self.i2 < len(self.v2):
                self.i2 += 1
                return self.v2[self.i2 - 1]
            else:
                self.i1 += 1
                return self.v1[self.i1 - 1]                  

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.i1 < len(self.v1) or self.i2 < len(self.v2)

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())