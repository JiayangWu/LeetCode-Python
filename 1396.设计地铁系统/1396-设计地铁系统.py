class UndergroundSystem(object):

    def __init__(self):
        from collections import defaultdict
        self.cnt = defaultdict(int)
        self.total = defaultdict(int)
        self.record = {} # key is id, val is the checkin stationName and time
    def checkIn(self, id, stationName, t):
        """
        :type id: int
        :type stationName: str
        :type t: int
        :rtype: None
        """
        self.record[id] = (stationName, t)

    def checkOut(self, id, stationName, t):
        """
        :type id: int
        :type stationName: str
        :type t: int
        :rtype: None
        """
        checkinStation = self.record[id][0]
        checkinTime = self.record[id][1]
        
        self.total[checkinStation + "#" + stationName] += t - checkinTime
        self.cnt[checkinStation + "#" + stationName] += 1


    def getAverageTime(self, startStation, endStation):
        """
        :type startStation: str
        :type endStation: str
        :rtype: float
        """
        return self.total[startStation + "#" + endStation] * 1.0 / self.cnt[startStation + "#" + endStation]


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)