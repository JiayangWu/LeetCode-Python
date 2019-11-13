from collections import defaultdict
from heapq import *
class Leaderboard(object):

    def __init__(self):
        self.dic = defaultdict(int)

    def addScore(self, playerId, score):
        """
        :type playerId: int
        :type score: int
        :rtype: None
        """
        self.dic[playerId] += score
        
    def top(self, K):
        """
        :type K: int
        :rtype: int
        """
        self.l = []
        heapify(self.l)
        for pid, score in self.dic.items():
            if len(self.l) >= K:
                if score > self.l[0]:
                    heappush(self.l, score)
                    heappop(self.l)       
            else:
                heappush(self.l, score)
                
        return sum(self.l)
                

    def reset(self, playerId):
        """
        :type playerId: int
        :rtype: None
        """
        self.dic[playerId] = 0

