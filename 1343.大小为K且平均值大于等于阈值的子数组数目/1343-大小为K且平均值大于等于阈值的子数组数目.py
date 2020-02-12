class Solution(object):
    def numOfSubarrays(self, arr, k, threshold):
        """
        :type arr: List[int]
        :type k: int
        :type threshold: int
        :rtype: int
        """
        res = 0
        target_sum = k * threshold
        subs = 0
        for i in range(0, k):
            subs += arr[i]
        
        for i in range(0, len(arr) - k + 1):
            if i:
                subs = subs - arr[i - 1] + arr[i + k - 1]
            if subs >= target_sum:
                res += 1
                
        return res