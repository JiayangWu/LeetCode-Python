class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        from collections import defaultdict
        res = []
        left = [] #存放没有在arr2里出现过的数字
        set2 = set(arr2) #把arr2转成set，让查找的时间复杂度降低到O(1)
       
        dic = defaultdict(int) #记录arr1中数字出现的频率
        for num in arr1:
            if num in set2:
                dic[num] += 1
            else:
                left.append(num)

        for num in arr2:
            res += [num] * dic[num]

        left.sort() #按照题目要求把没出现过的元素排序
        return res + left
            