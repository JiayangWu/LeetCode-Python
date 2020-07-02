class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        s = sum(nums)
        if s % k != 0 or len(nums) < k:
            return False
        
        target = s / k
        
        nums.sort(reverse = True)
        visited = set()
        
        self.res = False
        def dfs(cnt, tmp, start):
            if tmp == target:
                dfs(cnt - 1, 0, 0)
                
            if cnt == 0:
                self.res = True
                return
            if not self.res:
                for i in range(start, len(nums)):
                    if i not in visited and tmp + nums[i] <= target:
                        visited.add(i)
                        dfs(cnt, tmp + nums[i], i + 1)
                        visited.remove(i)
        dfs(k, 0, 0)
        return self.res
                    

            
            
            
            
            