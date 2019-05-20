class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        five = ten = 0
        for num in bills:
            if num == 5:
                five += 1
            elif num == 10 and five:
                ten += 1
                five -= 1
            elif num == 20 and five and ten:
                five -= 1
                ten -= 1
            elif num == 20 and five >= 3:
                five -= 3
            else:
                return False
        return True