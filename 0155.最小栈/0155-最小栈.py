class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_stack = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.append(x)
        if self.min_stack and self.min_stack[-1] <= x:
            self.min_stack.append(self.min_stack[-1])
        else:
            self.min_stack.append(x)
        

    def pop(self):
        """
        :rtype: void
        """
        self.stack = self.stack[:-1]
        self.min_stack = self.min_stack[:-1]
        

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.min_stack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()