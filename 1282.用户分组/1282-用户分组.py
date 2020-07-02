class Solution(object):
    def groupThePeople(self, groupSizes):
        """
        :type groupSizes: List[int]
        :rtype: List[List[int]]
        """
        from collections import defaultdict
        dic = defaultdict(list)

        res = []
        for i, x in enumerate(groupSizes):
            if x not in dic or len(dic[x]) < x:
                dic[x].append(i)
            if len(dic[x]) == x:
                res.append(dic[x])
                dic[x] = []
        
        return res