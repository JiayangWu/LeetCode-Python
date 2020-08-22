class Solution(object):
    def getWinner(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        winner = max(arr[0], arr[1])
        cnt = 1
        for num in arr[2:]:
            if cnt == k:
                return winner
            if winner > num:
                cnt += 1
            else:
                #刷新winner
                winner = num 
                cnt = 1
        return winner