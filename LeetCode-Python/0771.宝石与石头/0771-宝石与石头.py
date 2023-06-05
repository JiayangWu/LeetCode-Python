class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewels = set(jewels)

        res = 0
        for stone in stones:
            if stone in jewels:
                res += 1

        return res