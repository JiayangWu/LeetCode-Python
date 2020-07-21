class Solution(object):
    def minDays(self, bloomDay, m, k):
        """
        :type bloomDay: List[int]
        :type m: int
        :type k: int
        :rtype: int
        """
        if m * k > len(bloomDay):
            return -1
        
        left, right = 1, max(bloomDay)
        while left <= right:
            mid = (left + right) // 2
            # print mid
            flowerCnt = 0
            dayCnt = 0
            for day in bloomDay:
                if day <= mid:
                    dayCnt += 1
                    if dayCnt >= k:
                        flowerCnt += 1
                        dayCnt = 0
                else:
                    dayCnt = 0
            # print flowerCnt
            if flowerCnt >= m:
                right = mid - 1
            else:
                left = mid + 1
        return left
                    