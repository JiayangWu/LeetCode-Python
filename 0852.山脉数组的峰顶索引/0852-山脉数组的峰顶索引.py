class Solution(object):
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        left = 0
        right = len(A) - 1
        while( left <= right):
            mid = left + (right - left) / 2
            if A[mid - 1] < A[mid] < A[mid + 1]:
                left = mid + 1
            elif A[mid - 1] > A[mid] > A[mid + 1]:
                right = mid -1
            else:
                break
        print mid
        return mid