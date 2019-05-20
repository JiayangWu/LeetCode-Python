class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.s1 = list()
        self.s2 = list()
        

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        self.s1.append(x)
        # for i in range(len(s1)):
        while(self.s1):
            self.s2.append(self.s1.pop())
        

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        return self.s2.pop(0)
        

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        return self.s2[0]

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return len(self.s2) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()