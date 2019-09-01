class Solution(object):
    def dietPlanPerformance(self, calories, k, lower, upper):
        """
        :type calories: List[int]
        :type k: int
        :type lower: int
        :type upper: int
        :rtype: int
        """
        res = 0
        s = sum(calories[: k])
        for start in range(0, len(calories) - (k - 1)):
            if start != 0:
                # print start, 
                s += calories[start + k - 1] -  calories[start - 1]
            # print s
            if s < lower:
                res -= 1
            elif s > upper:
                res += 1
        return res