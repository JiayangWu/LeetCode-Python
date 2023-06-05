class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        res = True
        for i, d in enumerate(distance):
            char = chr(ord("a") + i)
            if s.count(char):
                if s.rfind(char) - s.index(char) != d + 1:
                    res = False
        return res