class ZigzagIterator(object):

    def __init__(self, v1, v2):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        self.list = []
        if v1 and v2:
            i = 0
            for i in range(min(len(v1), len(v2))):
                self.list.append(v1[i])
                self.list.append(v2[i])
            if v1[i + 1:]:
                self.list += v1[i + 1:]
            else:
                self.list += v2[i + 1:]
            
        elif v1:
            self.list = v1
        else:
            self.list = v2
        self.index = 0
    def next(self):
        """
        :rtype: int
        """
        self.index += 1
        return self.list[self.index - 1]

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.index != len(self.list)
        

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())