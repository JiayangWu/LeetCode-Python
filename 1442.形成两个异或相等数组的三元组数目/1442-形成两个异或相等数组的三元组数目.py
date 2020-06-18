class Solution(object):
    def countTriplets(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        leftXOR = [0 for _ in arr] + [0]

        res = 0
        
        for i, x in enumerate(arr):
            leftXOR[i + 1] = leftXOR[i] ^ x

        for i in range(len(arr) + 1):
            for j in range(i + 1, len(arr) + 1):
                for k in range(j + 1, len(arr) + 1):
                    if leftXOR[i] ^ leftXOR[j] == leftXOR[j] ^ leftXOR[k]:
                        res += 1

        return res