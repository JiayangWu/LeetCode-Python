class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """
        empty = res = numBottles
        while empty >= numExchange:
            res += empty / numExchange 
            empty = empty / numExchange + empty % numExchange
        return res
        