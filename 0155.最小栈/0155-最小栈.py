class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.s = []
        self.min_s = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.s.append(x)
        if self.min_s:
            self.min_s.append(min(x, self.min_s[-1]))
        else:
            self.min_s.append(x)

    def pop(self):
        """
        :rtype: None
        """
        self.min_s.pop()
        self.s.pop()


    def top(self):
        """
        :rtype: int
        """
        return self.s[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.min_s[-1]
    

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()