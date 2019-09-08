class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        idx = 0
        for i in range(len(gas)):
            if i < idx:
                continue
            j = i
            left_gas = gas[i]
            while left_gas > 0:
                # print j
                if left_gas < cost[j]: #去不了下一站
                    idx = max(idx, j)
                    break
                left_gas -= cost[j]
                if (j + 1) % len(gas) == i:
                    return i
                
                j = (j + 1) % len(gas)
                left_gas += gas[j]
        return -1
                
            