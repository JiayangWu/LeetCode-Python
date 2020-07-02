class Solution(object):
    def maxAliveYear(self, birth, death):
        """
        :type birth: List[int]
        :type death: List[int]
        :rtype: int
        """
        bucket = [0 for _ in range(102)]
        
        for i in range(len(birth)):
            bucket[birth[i] - 1900] += 1
            bucket[death[i] + 1 - 1900] -= 1
        
        maxx, res = 0, 0
        for i in range(1, len(bucket)):
            bucket[i] += bucket[i - 1]
            if bucket[i] > maxx:
                maxx = bucket[i]
                res = i
        
        return res + 1900