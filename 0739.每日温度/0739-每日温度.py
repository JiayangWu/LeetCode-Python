class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        res = [0] * len(T)
        s = []
        # print res
        for i in range(0, len(T)):
            while(s and T[i] > T[s[-1]]):
                res[s[-1]] = i - s[-1]
                s.pop()
            s.append(i)            
        return res