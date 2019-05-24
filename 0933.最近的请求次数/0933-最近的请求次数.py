from collections import deque
class RecentCounter(object):
    def __init__(self):
        self.queue = deque()

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        self.queue.append(t)
        
        while(self.queue[0] < t - 3000):
            self.queue.popleft()

        return len(self.queue) 
