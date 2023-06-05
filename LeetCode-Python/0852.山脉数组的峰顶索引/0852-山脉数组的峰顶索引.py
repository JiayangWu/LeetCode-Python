class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = (left + right) // 2
            if 0 < mid < len(arr) - 1 and arr[mid - 1] < arr[mid] and arr[mid] > arr[mid + 1]:
                return mid

            if arr[mid + 1] > arr[mid]:
                left = mid + 1
            else:
                right = mid - 1
        return left