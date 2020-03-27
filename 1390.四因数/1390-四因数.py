class Solution(object):
    def sumFourDivisors(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def factor(n):
            l = []
            for i in range(1, int(n ** 0.5) + 1):
                if n % i == 0:
                    l.append(i)
                    if n / i != i:
                        l.append(n / i)
                if len(l) > 4:
                    break

            return sum(l) if len(l) == 4 else 0 

        return sum(map(factor, nums))