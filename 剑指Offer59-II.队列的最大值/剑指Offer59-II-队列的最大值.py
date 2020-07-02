class MaxQueue(object):

    def __init__(self):
        from collections import deque
        self.queue = deque([])
    def max_value(self):
        """
        :rtype: int
        """
        if self.queue:
            return max(self.queue)
        return -1
    
    def push_back(self, value):
        """
        :type value: int
        :rtype: None
        """
        self.queue.append(value)


    def pop_front(self):
        """
        :rtype: int
        """
        if not self.queue:
            return -1
        return self.queue.popleft()


# Your MaxQueue object will be instantiated and called as such:
# obj = MaxQueue()
# param_1 = obj.max_value()
# obj.push_back(value)
# param_3 = obj.pop_front()