class Solution(object):
    def maxSatisfied(self, customers, grumpy, X):
        """
        :type customers: List[int]
        :type grumpy: List[int]
        :type X: int
        :rtype: int
        """
        record = [0 for _ in range(len(grumpy))] #代表在i满意的顾客总数
        s = 0
        for i in range(len(grumpy)):
            if grumpy[i] == 0:
                record[i] += record[i - 1] + customers[i]
            else:
                record[i] += record[i - 1]
                
        print record       
        tmp =  record[-1]#不生气的时候已经可以满足的

        prefix = [0 for _ in range(len(grumpy))]
        prefix[0] = customers[0]
        
        for i in range(1, len(grumpy)):
            prefix[i] += prefix[i - 1] + customers[i]

        lo, hi = 0, X - 1
        newcus = 0
        print prefix
        while(hi < len(grumpy)):
            if lo == 0:
                presum = prefix[hi] - 0 #上了BUFF之后的
                angsum = record[hi] - 0 #没上BUFF
            else:
                presum = prefix[hi] - prefix[lo - 1]
                angsum = record[hi] - record[lo - 1]  
            
            earn = presum - angsum
            print presum, angsum, earn, hi
            newcus = max(presum - angsum, newcus)
            hi += 1
            lo += 1
        return tmp + newcus
            
            
                