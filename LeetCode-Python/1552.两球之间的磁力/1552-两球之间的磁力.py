class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        left, right = 1, position[-1] - position[0]
        while left <= right:
            mid = (left + right) // 2 # target answer

            cnt, prev = 1, position[0]
            for p in position:
                if prev + mid <= p: # find another possible position
                    cnt += 1
                    prev = p

            if cnt >= m:
                left = mid + 1
            elif cnt < m:
                right = mid - 1
        return right