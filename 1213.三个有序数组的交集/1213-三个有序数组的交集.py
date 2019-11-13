class Solution(object):
    def arraysIntersection(self, arr1, arr2, arr3):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :type arr3: List[int]
        :rtype: List[int]
        """
        res = []
        record = [0 for _ in range(2005)]
        for num in arr1 + arr2 + arr3:
            record[num] += 1
        
        for i in range(len(record)):
            if record[i] == 3:
                res.append(i)
                
        return res