class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        n = len(citations)
        left, right = 0, len(citations) - 1
        res = 0
        while left <= right:
            
            mid = (left + right) // 2
            
            cnt = n - mid
            # print left, right, mid, citations[mid], cnt, citations
            if citations[mid] < cnt:
                left = mid + 1
            elif citations[mid] >= cnt:
                res = cnt
                right = mid - 1
        return res