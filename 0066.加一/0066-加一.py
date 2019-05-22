class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        index = 0
        if digits[-1] != 9:
            digits[-1] += 1
            return digits
        else:
            for index in range(len(digits)-1, -1,-1):
                if digits[index] != 9:
                    break
            if digits[index] != 9:
                digits[index] += 1
                for i in range(index+ 1, len(digits)):
                    digits[i] = 0
                return digits
            else:
                res = [1]
                for i in range(0,len(digits)):
                    res.append(0)
                return res