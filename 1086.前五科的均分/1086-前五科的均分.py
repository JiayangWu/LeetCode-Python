import heapq
class Solution(object):
    def highFive(self, items):
        """
        :type items: List[List[int]]
        :rtype: List[List[int]]
        """
        record = dict()
        
        for item in items:
            sd, sc = item[0], item[1]
            
            if sd not in record:
                record[sd] = [sc]
                heapq.heapify(record[sd])
            else:
                heapq.heappush(record[sd], sc)
                if len(record[sd]) > 5:
                    heapq.heappop(record[sd])
                    print record[sd]
        res = []
        for key, val in record.items():
            res.append([key, sum(val) // 5])
        # print record
        return res
        