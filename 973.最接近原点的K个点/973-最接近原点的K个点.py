class Solution(object):
    def kClosest(self, points, K):
        left, right, target = 0, len(points) - 1, K - 1
        while True:
            pos = self.partition(points, left, right)
            if pos == target:
                return points[:pos + 1]
            elif pos > K: #要往左找
                right = pos - 1
            elif pos < K: #要往右找
                left = pos + 1
                
    def partition(self, nums, left, right):
        import random
        k = random.randint(left, right)
        pivot = nums[k][0] ** 2 + nums[k][1] ** 2
        nums[left], nums[k] = nums[k], nums[left]
        index = left
        
        for i in range(left + 1, right + 1):
            if nums[i][0] ** 2 + nums[i][1] ** 2 < pivot:
                index += 1
                nums[i], nums[index] = nums[index], nums[i]
        nums[left], nums[index] = nums[index], nums[left]
        return index #此时所有index左侧的值都比nums[index]大， 所有右侧的值都比nums[index]小
