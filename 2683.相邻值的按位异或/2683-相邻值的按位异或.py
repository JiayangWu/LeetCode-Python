class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        cur = 0
        for i, n in enumerate(derived):
            if i != len(derived) - 1:
                if n == 1:
                    cur = 1 - cur
            else:
                return 0 ^ cur == n