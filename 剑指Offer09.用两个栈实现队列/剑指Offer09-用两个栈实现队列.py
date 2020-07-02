class CQueue(object):

    def __init__(self):
        self.s1 = []
        self.s2 = []

    def appendTail(self, value):
        """
        :type value: int
        :rtype: None
        """
        self.s1.append(value)

    def deleteHead(self):
        """
        :rtype: int
        """
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2.pop() if self.s2 else -1
        


# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()