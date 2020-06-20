class Solution(object):
    def peopleIndexes(self, favoriteCompanies):
        """
        :type favoriteCompanies: List[List[str]]
        :rtype: List[int]
        """
        from collections import defaultdict
        
        dic = defaultdict(set)
        
        for i, l in enumerate(favoriteCompanies):
            for company in l:
                dic[company].add(i)

        res = []
        for i, l in enumerate(favoriteCompanies):
            s = dic[l[0]]
            for company in l[1:]:
                # print i,s, dic[company]
                s = s & dic[company]
                # print s
            # print i, s
            if len(s) == 1:
                res.append(i)
                
        return res
        