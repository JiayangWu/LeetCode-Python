class Solution(object):
    def numPairsDivisibleBy60(self, time):
        """
        :type time: List[int]
        :rtype: int
        """
        record = [0 for _ in range(0, 60)]
        for index, item in enumerate(time):
            record[item % 60] += 1

        res = 0
        for i in range(0, 60):
            if i in [0, 30] and record[i] > 1:
                res += record[i] * (record[i] - 1) # 对于N个可以被60整除的数来说，在它们中取得所有结果的个数为C N 2 = N *(N - 1) / 2
                record[i] = 0 # 一次处理完所有的可以被60整除的数，然后把record[0]归零，保证不重复计算
            elif i:            
                res += record[60 - i] * record[i]

        return res // 2