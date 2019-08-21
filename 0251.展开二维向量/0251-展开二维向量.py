class Vector2D(object):

    def __init__(self, v):
        """
        :type v: List[List[int]]
        """
        self.list = []
        for item in v:
            for num in item:
                self.list.append(num)
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
        return self.index < len(self.list)


# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(v)
# param_1 = obj.next()
# param_2 = obj.hasNext()