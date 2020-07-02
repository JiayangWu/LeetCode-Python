class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        m, n = len(nums), len(nums[0])
        if r * c != m * n:
            return nums
        nums = sum(nums, [])

        res = [[0 for _  in range(c)]  for _ in range(r)]

        for i in range(r):
            for j in range(c):
                res[i][j] = nums[i * c + j]
        
        return res