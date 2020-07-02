class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_s = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if not self.stack:
            self.stack = [x]
            self.min_s = [x]
        else:
            self.stack.append(x)
            if self.min_s[-1] < x:
                self.min_s.append(self.min_s[-1])
            else:
                self.min_s.append(x)

    def pop(self):
        """
        :rtype: None
        """
        self.stack.pop()
        self.min_s.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def min(self):
        """
        :rtype: int
        """
        return self.min_s[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.min()