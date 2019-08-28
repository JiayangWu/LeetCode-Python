class Solution(object):
    def minCostII(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        if not costs:
            return 0
        
        def helper(last, k):
            res = max(last)
            for i in range(len(last)):
                if i != k:
                    res = min(res, last[i])
            return res
        
        for i in range(1, len(costs)):
            row = costs[i]
            for j in range(len(row)):
                row[j] += helper(costs[i - 1], j)
        return min(costs[-1])