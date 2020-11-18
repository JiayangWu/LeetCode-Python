class UndergroundSystem(object):

    def __init__(self):
        self.check_in_history = dict() # key is id + stationName, val is t
        self.StationTraverlTime = dict()
    def checkIn(self, id, stationName, t):
        """
        :type id: int
        :type stationName: str
        :type t: int
        :rtype: None
        """
        self.check_in_history[str(id)] = [stationName, t]


    def checkOut(self, id, stationName, t):
        """
        :type id: int
        :type stationName: str
        :type t: int
        :rtype: None
        """
        start_station, start_time = self.check_in_history[str(id)]
        self.check_in_history.pop(str(id))
        time_spent = t - start_time
        key = start_station + "#" + stationName
        if key not in self.StationTraverlTime:
            self.StationTraverlTime[key] = [time_spent,1]
        else:
            self.StationTraverlTime[key][0] += time_spent
            self.StationTraverlTime[key][1] += 1


    def getAverageTime(self, startStation, endStation):
        """
        :type startStation: str
        :type endStation: str
        :rtype: float
        """
        key = startStation + "#" + endStation
        return self.StationTraverlTime[key][0] * 1.0 / self.StationTraverlTime[key][1]


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)