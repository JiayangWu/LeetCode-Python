class Solution(object):
    def isPossibleDivide(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        from collections import Counter, deque
        dic = Counter(nums)
        nums = deque(sorted(list(set(nums))))

        res = []
        while nums:
            num = nums[0]
            for i in range(k):
                target = num + i 
                if target not in dic:
                    return False
                dic[target] -= 1
                if dic[target] == 0:
                    nums.popleft()
        return True