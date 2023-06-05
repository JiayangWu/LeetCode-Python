class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        left, right = max(nums), sum(nums)
        while left <= right:
            mid = (left + right) // 2 # target answer

            subarray_cnt, cur_sum = 1, 0
            for num in nums:
                if cur_sum + num <= mid:
                    cur_sum += num
                else:
                    subarray_cnt += 1
                    cur_sum = num

            if subarray_cnt <= k: # need to get more subarrays
                right = mid - 1
            elif subarray_cnt > k:
                left = mid + 1
        return left