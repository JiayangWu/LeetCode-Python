class Solution(object):
    def numOfSubarrays(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        prefix_sum = [0 for _ in arr]
        prefix_sum[0] = arr[0]

        for i in range(1, len(arr)):
            prefix_sum[i] = prefix_sum[i - 1] + arr[i]

        MOD = 10 ** 9 + 7
        even, odd = 1, 0
        res = 0
        for i in range(len(arr)):
            if prefix_sum[i] % 2 == 0:
                res += odd 
                even += 1
            else:
                res += even
                odd += 1
            res = res % MOD 
        return res 
            