class Solution(object):
    def maximizeSweetness(self, sweetness, K):
        """
        :type sweetness: List[int]
        :type K: int
        :rtype: int
        """
        if not K:
            return sum(sweetness)
        left, right = 0, sum(sweetness) // K
        res = 0
        while left <= right:
            mid = (left + right) // 2
            cnt = 0
            tmp = 0
            for s in sweetness:
                if tmp + s > mid:
                    cnt += 1
                    tmp = 0
                else:
                    tmp += s
            
            if cnt < K + 1:
                right = mid - 1
            else:
                left = mid + 1
        return left