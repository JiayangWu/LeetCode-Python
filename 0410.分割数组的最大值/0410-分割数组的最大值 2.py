class Solution(object):
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        # min(nums), sum(nums)
        if len(nums) == m:
            return max(nums)
        lo, hi = max(nums), sum(nums)
        while(lo < hi):
            mid = (lo + hi) // 2 # ����
            
            temp, cnt = 0, 1
            for num in nums:
                temp += num
                # cnt += 1
                if temp > mid:
                    temp = num
                    cnt += 1
            # print temp, cnt, mid
            
            if cnt > m: #�����˼�����˵��midӦ�üӴ�
                lo = mid + 1
            elif cnt <= m:
                hi = mid

                
        return lo
            