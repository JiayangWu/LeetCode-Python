class Solution(object):
    def rangeSum(self, nums, n, left, right):
        """
        :type nums: List[int]
        :type n: int
        :type left: int
        :type right: int
        :rtype: int
        """
        res = []
        for i in range(n):
            for j in range(i + 1, n + 1):
                res.append(sum(nums[i:j]))
        res.sort()
        # print res
        return sum(res[left - 1:right]) % (10 ** 9 + 7)
                
                