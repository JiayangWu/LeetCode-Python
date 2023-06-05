class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # sliding window
        from collections import defaultdict
        k = min(k, len(nums))
        left, right = 0, k + 1
        num2freq = defaultdict(int)

        for index in range(left, right):
            if index < len(nums):
                num = nums[index]
                num2freq[num] += 1
                if num2freq[num] > 1:
                    return True

        while right < len(nums):
            # [left, right)
            num2freq[nums[left]] -= 1
            num2freq[nums[right]] += 1
            if num2freq[nums[right]] > 1:
                return True
            right += 1
            left += 1
        return False