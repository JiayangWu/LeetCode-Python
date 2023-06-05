class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        bucket = [0 for _ in range(2 * (10 ** 4) + 1)]

        for num in nums:
            bucket[num + 10 ** 4] += 1
        
        cur = 0
        for index, count in enumerate(bucket):
            if count:
                # print(index, count)
                cur += count
                if cur >= (len(nums) - k + 1):
                    return index - 10 ** 4
        