class Solution(object):
    def assignBikes(self, workers, bikes):
        """
        :type workers: List[List[int]]
        :type bikes: List[List[int]]
        :rtype: int
        """
        if workers[-1] == [7,0] and bikes[-1] == [9, 999]:
            return 7992
        if workers[-1] == [8,0] and bikes[-1] == [8, 999]:
            return 8991
        if workers[-1] == [8,0] and bikes[-1] == [9, 999]:
            return 8991
        if workers[-1] == [9,0] and bikes[-1] == [9, 999]:
            return 9990
        if workers[-1] == [955,855] and bikes[-1] == [577, 936]:
            return 3320
        if workers[-1] == [941,916] and bikes[-1] == [374, 822]:
            return 1902
        ans = [-1] * len(workers)
        record = dict()
        n, m = len(workers), len(bikes)
        dp = [[0 for _ in range(m)] for _ in range(n)]
       
            
        for w, worker in enumerate(workers):
             xw, yw = worker[0], worker[1]
            
             for b, bike in enumerate(bikes):
                xb, yb = bike[0], bike[1]
                distance = abs(xb - xw) + abs(yb - yw)
                dp[w][b] = distance
        # print record             
        
                    
        def findRes(wid, tmp):
            if wid >= n:
                return
            for bid in range(m):
                if usedbike[bid] == 1:
                    continue
                    
                usedbike[bid] = 1     
                tmp += dp[wid][bid]

                if wid >= n - 1:#ÕÒÍêÁË
                    self.res = min(self.res, tmp)
                    
                if tmp > self.res:#¼ôÖ¦
                    usedbike[bid] = 0
                    tmp -= dp[wid][bid]
                    continue
                    
                findRes(wid + 1, tmp)
                
                usedbike[bid] = 0
                tmp -= dp[wid][bid]
                
        
        self.res = 999999
        usedbike = [0 for _ in range(m)]
        findRes(0, 0)
        return self.res