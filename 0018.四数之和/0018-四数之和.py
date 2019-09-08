class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if len(nums) < 4:
            return []
        nums.sort()
        res = []
        def findThreeSum(num, l, t):
            for i, n in enumerate(l):
                if i == 0 or l[i] > l[i - 1]:
                    left, right = i + 1, len(l) - 1
                    while(left < right):
                        s = n + l[left] + l[right]

                        if s == t:
                            res.append([num, n, l[left], l[right]])
                            left += 1
                            right -= 1
                            while(left < right and l[left] == l[left - 1]):
                                left += 1
                            while(right > left and l[right] == l[right + 1]):
                                right -= 1
                        elif s > t:
                            right -= 1
                        else:
                            left += 1
                      
        for i, num in enumerate(nums):
            if i == 0 or nums[i] > nums[i - 1]:
                findThreeSum(num, nums[i + 1:], target - num)
                
        return res
        