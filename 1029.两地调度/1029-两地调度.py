class Solution(object):
    def twoCitySchedCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        costs = sorted(costs, key = lambda x: x[0] - x[1])
        
        res,n = 0, len(costs) // 2
        for i in range(n):
            res += costs[i][0] + costs[i + n][1]
                
        return res