from heapq import *
class Solution(object):
    def largestValsFromLabels(self, values, labels, num_wanted, use_limit):
        """
        :type values: List[int]
        :type labels: List[int]
        :type num_wanted: int
        :type use_limit: int
        :rtype: int
        """
        record = dict()
        l = len(values)
        for i in range(l):
            if labels[i] not in record:
                record[labels[i]] = [values[i]]
                heapify(record[labels[i]])
            else:
                heappush(record[labels[i]], values[i])
                if len(record[labels[i]]) > use_limit:
                    heappop(record[labels[i]])
                    
        res = []
        for key, val in record.items():
            res += val
        res.sort()
        return sum(res[-num_wanted:])
                    