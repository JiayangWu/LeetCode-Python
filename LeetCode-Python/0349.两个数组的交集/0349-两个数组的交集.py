class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        nums2.sort()
        res = set()
        for num in nums1:
            if num not in res:
                # search num in nums2
                left, right = 0, len(nums2) - 1
                while left <= right:
                    mid = (left + right) // 2
                    if nums2[mid] == num:
                        res.add(num)
                        break
                    elif nums2[mid] < num:
                        left = mid + 1
                    else:
                        right = mid - 1
        return list(res)