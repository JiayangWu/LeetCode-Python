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
            elif pos > k: #Ҫ������
                right = pos - 1
            elif pos < k: #Ҫ������
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
        return index #��ʱ����index����ֵ����nums[index]�� �����Ҳ��ֵ����nums[index]С