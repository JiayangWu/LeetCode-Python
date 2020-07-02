class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        prefix = []
        
        for i, num in enumerate(nums):
            if i:
                prefix.append(num + prefix[-1])
            else:
                prefix.append(num)

        res = 0
        dic = collections.defaultdict(int)
        dic[0] = 1
        for s in prefix:
            res += dic[s - k]
            dic[s] += 1
        return res