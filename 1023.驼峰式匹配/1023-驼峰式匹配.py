class Solution(object):
    def camelMatch(self, queries, pattern):
        """
        :type queries: List[str]
        :type pattern: str
        :rtype: List[bool]
        """
        # hashq = [collections.Counter(x) for i, x in enumerate(queries)]
        # hashp = collections.Counter(pattern)
        maxp  = len(pattern)
        res = list()
        for query in queries:
            # print "~~~~~~~~~~~~~~~~~"
            p, q = 0, 0
            maxq = len(query)
            while p < maxp:
                # print p, q, query[q], pattern[p]
                if q + maxp - p - 1 >= maxq: #maxp - p - 1
                    res.append(False)
                    break
                if query[q] == pattern[p]:#匹配上了
                    q += 1
                    p += 1
                    if p == maxp:#pattern全部匹配上了，而且query后面的都是小写，符合要求
                        flag = 1
                       
                        for char in query[q + 1:]:
                            if char.isupper():
                                flag = 0                              
                        if flag:                            
                            res.append(True)
                        else:
                            res.append(False)
                            
                elif query[q].isupper():#q大写，P对不上，肯定不对
                    res.append(False)
                    break
                else:
                    q += 1
                # print res, query   
            # if q == maxq - 1 and p == maxp - 1:
            #     res.append(True)
                
        return res
                
        