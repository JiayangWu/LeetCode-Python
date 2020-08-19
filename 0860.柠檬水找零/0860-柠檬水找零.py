class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        dic = {5:0, 10:0}

        for bill in bills:
            if bill == 5:
                dic[5] += 1
            elif bill == 10:
                if dic[5] < 1:
                    return False
                dic[5] -= 1
                dic[10] += 1
            else:
                if dic[10] and dic[5]:
                    dic[10] -= 1
                    dic[5] -= 1
                elif dic[5] >= 3:
                    dic[5] -= 3
                else:
                    return False
        return True
