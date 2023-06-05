class Solution:
    def memLeak(self, memory1: int, memory2: int) -> List[int]:
        res = []
        memory = 1
        while memory1 or memory2:
            if memory1 >= memory2:
                if memory1 < memory:
                    break
                else:
                    memory1 -= memory
            else:
                if memory2 < memory:
                    break
                else:
                    memory2 -= memory
                
            memory += 1
        return [memory, memory1, memory2]