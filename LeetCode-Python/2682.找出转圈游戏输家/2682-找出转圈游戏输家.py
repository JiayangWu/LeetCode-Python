class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        visited = set()
        cur, cnt = 1, 1
        while cur not in visited:
            visited.add(cur)
            cur = cur + k * cnt
            while cur > n:
                cur = cur - n
            cnt += 1

        return [i for i in range(1, n + 1) if i not in visited]