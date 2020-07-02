class Solution(object):
    def displayTable(self, orders):
        """
        :type orders: List[List[str]]
        :rtype: List[List[str]]
        """
        from collections import defaultdict
        dishes = set()
        tables = set()
        dic = dict()
        
        for c, t, f in orders:
            dishes.add(f)
            tables.add(int(t))
            
            if t not in dic:
                dic[t] = defaultdict(int)
            dic[t][f] += 1

        dishes = sorted(list(dishes))
        res = [["Table"] + dishes]

        for t in sorted(list(tables)):
            tmp = [str(t)]
            for d in dishes:
                tmp.append(str(dic[str(t)][d]))
            res.append(tmp)
        return res
            
        