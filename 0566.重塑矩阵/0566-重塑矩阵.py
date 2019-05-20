class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        m, n = len(nums), len(nums[0])
        if m * n != c * r:
            return nums
        
        l = list()
        for row in nums:
            for item in row:
                l.append(item)
                
        cnt = 0
        res = list()
        for i in range(r):
            temp = list()
            for j in range(c):
                temp.append(l[cnt])
                cnt += 1
            res.append(temp)
            
        return res