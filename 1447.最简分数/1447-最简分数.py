class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        import math
        res = set()
        
        for down in range(1, n + 1):
            for up in range(1, down):
                if math.gcd(up, down) == 1:
                    res.add(str(up) + "/" + str(down))
                    
        return list(res)