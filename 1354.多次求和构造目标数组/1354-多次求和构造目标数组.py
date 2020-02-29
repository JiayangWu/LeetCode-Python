class Solution(object):
    def isPossible(self, target):
        """
        :type target: List[int]
        :rtype: bool
        """
        from heapq import *
        if len(target) == 1:
            return target[0] == 1
   
        s = sum(target)
        target = [-item for item in target]
        heapify(target)
        
        while s > len(target):
            # 找当前最大的数和第二大的数
            m = -heappop(target)
            s_m = -target[0]

            # 更新 m 并更新 s
            diff = s - m             
            if not diff:
                break
            new_m = m - (max(1, (m - s_m) / diff) * diff)
            s = s - m + new_m

            heappush(target, -new_m)

        return not any([num != -1 for num in target])