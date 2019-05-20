class Solution(object):
    def minEatingSpeed(self, piles, H):
        """
        :type piles: List[int]
        :type H: int
        :rtype: int
        """
        import math
        #max(piles), 1
        if len(piles) == 1:
            return int(math.ceil(piles[0] // H) + 1)
        lo, hi = math.ceil(sum(piles)/H), max(piles)
        while(lo < hi):
            mid = (lo + hi)// 2
            
            cnt = 0
            for pile in piles:
                cnt += math.ceil(pile / mid)
                # print cnt
                    
            # print k, cnt
            if cnt > H:# ณิตรยýมห
                lo = mid + 1
            elif cnt <= H:
                hi = mid
                
        return int(lo)
                