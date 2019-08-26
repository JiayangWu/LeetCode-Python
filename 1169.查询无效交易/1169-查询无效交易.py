class Solution(object):
    def invalidTransactions(self, transactions):
        """
        :type transactions: List[str]
        :rtype: List[str]
        """
        recordByName = collections.defaultdict(list)
        for trans in transactions:
            name, time, amount, city = trans.split(",")
            recordByName[name].append([name, int(time), int(amount), city])
        
        def convert(l): 
            return l[0] + "," + str(l[1]) + "," + str(l[2]) + "," + l[3]
        
        res = set()
        for name, rec in recordByName.items():
            curRec = sorted(rec, key = lambda x:x[1])
            
            for i in range(len(curRec)):
                if curRec[i][2] > 1000:
                    res.add(convert(curRec[i]))
                for j in range(i + 1, len(curRec)):
                    
                    if abs(curRec[j][1] - curRec[i][1]) > 60:  
                        break
                    if curRec[j][3] != curRec[i][3]:
                        res.add(convert(curRec[i]))
                        res.add(convert(curRec[j]))
        return res
                        
                        
                