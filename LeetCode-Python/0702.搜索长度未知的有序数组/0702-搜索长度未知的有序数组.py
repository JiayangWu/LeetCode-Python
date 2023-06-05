# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader:
#    def get(self, index: int) -> int:

class Solution:
    def search(self, reader: 'ArrayReader', target: int) -> int:
        OVERFLOW = 2 ** 31 - 1
        left, right = 0, 10 ** 4
        while left <= right:
            mid = (left + right) // 2
            returned_val = reader.get(mid)
            if returned_val == OVERFLOW:
                right = mid - 1
                continue
            if returned_val == target:
                return mid
            elif returned_val > target:
                right = mid - 1
            else:
                left = mid + 1
        return -1
            