class Solution(object):
    def findInMountainArray(self, target, mountain_arr):
        """
        :type target: integer
        :type mountain_arr: MountainArray
        :rtype: integer
        """
        # 得到数组长度
        n = mountain_arr.length()  
        #找山顶
        left, right = 0, n - 1
        while 1:
            mid = (left + right) // 2
            val = mountain_arr.get(mid)
            lval, rval = mountain_arr.get(mid - 1), mountain_arr.get(mid + 1)

            if val > lval and val > rval:
                peak = val
                peak_idx = mid
                break
            if val < rval:
                left = mid + 1
            else:
                right = mid
        if target == peak:
            return mid

        #找左侧
        left, right = 0, peak_idx - 1
        while left <= right:
            mid = (left + right) // 2
            val = mountain_arr.get(mid)
            if val == target:
                return mid
            elif val > target:
                right = mid - 1
            else:
                left = mid + 1
                
        #找右侧
        left, right = peak_idx + 1, n - 1
        while left <= right:
            mid = (left + right) // 2
            val = mountain_arr.get(mid)
            if val == target:
                return mid
            elif val > target:
                left = mid + 1
            else:     
                right = mid - 1
                
        return -1    
