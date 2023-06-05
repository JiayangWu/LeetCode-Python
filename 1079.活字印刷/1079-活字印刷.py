class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        res = set([""])

        for tile in tiles:
            new_res = set()
            for r in res:
                for i in range(len(r) + 1):
                    t = r[:i] + tile + r[i:]
                    if t not in res:
                        new_res.add(t)
            res = res.union(new_res)

        return len(res) - 1