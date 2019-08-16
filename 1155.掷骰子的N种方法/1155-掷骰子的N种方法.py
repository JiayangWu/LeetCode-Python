class Solution(object):
    def numRollsToTarget(self, d, f, target):
        """
        :type d: int
        :type f: int
        :type target: int
        :rtype: int
        """
        record = dict()
        def backtrack(dice, face, t):
            if (dice, face, t) in record: #如果已经知道当前问题的解
                return record[(dice, face, t)] #直接读取即可
            
            if dice == 0: #当没有骰子的时候，判断一下是不是刚好找到target
                return 1 if t == 0 else 0
            
            if t < 0 or dice <= 0: #无效的时候没有解，所以返回0
                return 0
            tmp = 0 #tmp用于记录当前问题有多少个解
            for i in range(1, face + 1): #尝试所有的组合
                tmp += backtrack(dice - 1, face, t - i) 
                
            record[(dice, face, t)] = tmp #把解存起来，方便以后用
            return tmp
        
        backtrack(d, f, target)
        return max(record.values()) % (10 ** 9 + 7) #最大的解就是母问题的解
                
            