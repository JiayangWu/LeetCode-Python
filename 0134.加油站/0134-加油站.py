class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        if sum(gas) < sum(cost) or not len(gas):
            return -1
        l = len(gas)
        sub = [gas[i] - cost[i] for i in range(l)]
        
        g = 0
        index = 0
        for i in range(l): #i是出发加油站的编号
            g = g + sub[i]
            if g < 0:
                g = 0
                index = i + 1
                
        return index
