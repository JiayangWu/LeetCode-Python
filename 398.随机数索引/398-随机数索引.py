class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        from collections import defaultdict
        self.dic = defaultdict(list)
        for i, num in enumerate(nums):
            self.dic[num].append(i)

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        return random.choice(self.dic[target])


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)