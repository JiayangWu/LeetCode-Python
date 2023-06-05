class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return sorted(nums)[::-1][k - 1]