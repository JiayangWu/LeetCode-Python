class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1, p2 = m - 1, n - 1
        index = m + n - 1
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] < nums2[p2]:
                nums1[index] = nums2[p2]
                p2 -= 1
            else:
                nums1[index] = nums1[p1]
                p1 -= 1
            index -= 1

        while p2 >= 0:
            nums1[index] = nums2[p2]
            p2 -= 1
            index -= 1

