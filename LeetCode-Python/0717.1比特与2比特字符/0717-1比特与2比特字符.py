class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        connected_with_prev = False

        for i, bit in enumerate(bits):
            if connected_with_prev:
                if i == len(bits) - 1:
                    return False
                connected_with_prev = False
            else:
                if bit == 1:
                    connected_with_prev = True
                else:
                    connected_with_prev = False
        return True            