class Solution(object):
    def totalMoney(self, n):
        """
        :type n: int
        :rtype: int
        """
        day_cnt = 1
        summ = 0
        for i in range(1, n + 1):
            if i % 7 == 1:
                day_cnt = i // 7 + 1
            summ += day_cnt
            day_cnt += 1

        return summ
