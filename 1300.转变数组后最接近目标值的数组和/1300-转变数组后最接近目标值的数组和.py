class Solution(object):
    def findBestValue(self, arr, target):
        """
        :type arr: List[int]
        :type target: int
        :rtype: int
        """
        left, right = 0, max(arr)
        sub, ans = float("inf"), float("inf")
        
        while left <= right:
            mid = (left + right) // 2 # mid 为本次猜测的答案
            
            tmp = 0 # tmp 是本次猜测新数组之和
            for num in arr:
                if num > mid:
                    tmp += mid
                else:
                    tmp += num
            
            cur_sub = abs(tmp - target) #当前差的最小值

            if cur_sub < sub: # 如果有更小的答案
                sub = cur_sub
                ans = mid
            elif cur_sub == sub:
                ans = min(ans, mid)

            if tmp > target:
                right = mid - 1
            elif tmp < target:
                left = mid + 1
            elif tmp == target:
                return mid
                
        return ans
        
        
            