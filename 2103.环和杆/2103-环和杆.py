class Solution:
    def countPoints(self, rings: str) -> int:
        from collections import defaultdict
        
        ring2color = defaultdict(set)
        for index in range(0, len(rings), 2):
            color, ring = rings[index], rings[index + 1]

            ring2color[ring].add(color)
        res = 0
        for ring, color in ring2color.items():
            if len(color) == 3:
                res += 1
        return res