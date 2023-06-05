class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        left, right, target = 0, len(nums) - 1, k - 1
        while True:
            pos = self.partition(nums, left, right)
            if pos == target:
                return nums[pos]
            elif pos > k: #要往左找
                right = pos - 1
            elif pos < k: #要往右找
                left = pos + 1
                
    def partition(self, nums, left, right):
        import random
        k = random.randint(left, right)
        pivot = nums[k]
        nums[left], nums[k] = nums[k], nums[left]
        index = left
        
        for i in range(left + 1, right + 1):
            if nums[i] > pivot:
                index += 1
                nums[i], nums[index] = nums[index], nums[i]
        nums[left], nums[index] = nums[index], nums[left]
        return index #此时所有index左侧的值都比nums[index]大， 所有右侧的值都比nums[index]小