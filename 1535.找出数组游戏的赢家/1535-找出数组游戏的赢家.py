class Solution(object):
    def getWinner(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        pre = max(arr[0], arr[1])
        cnt = 1
        for num in arr[2:]:
            if cnt == k:
                return pre
            if pre > num:
                cnt += 1
            else:
                pre = num 
                cnt = 1
        return pre
            