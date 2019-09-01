class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        def helper(num):
            n = int(num)
            num = str(n)
            if n < 100:
                return subhelper(num)
            else:
                return ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"][int(num[0]) - 1] + " Hundred " + subhelper(num[1:]) if num[1:] != "00" else ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"][int(num[0]) - 1] + " Hundred"
            
        def subhelper(num):
            n = int(num)
            l1 = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
            l2 = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
            l3 = ["Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
            if n < 10:
                return l1[int(num)]
            if 10 <= n < 20:
                return l2[n - 10]
            if 20 <= n < 100:
                return l3[int(num[0]) - 2] + " " + l1[int(num[1])] if num[1] != "0" else l3[int(num[0]) - 2]
        res = ""
        if num >= 1000000000:
            res = helper(str(num)[0]) + " Billion"
            if str(num)[1:4] != "000":
                res += " " + helper(str(num)[1:4]) + " Million"
            if str(num)[4:7] != "000":
                res += " " + helper(str(num)[4:7]) + " Thousand"
            if str(num)[7:] != "000":
                res += " " + helper(str(num)[7:])
        elif num >= 1000000:
            res = helper(str(num)[:-6]) + " Million"
            if str(num)[-6:-3] != "000":
                res += " " + helper(str(num)[-6:-3]) + " Thousand"
            if str(num)[-3:] != "000":
                res += " " + helper(str(num)[-3:])
        elif num >= 1000:
            res = helper(str(num)[:-3]) + " Thousand"
            if str(num)[-3:] != "000":
                res += " " + helper(str(num)[-3:])
        else:
            return helper(str(num))
            
        return res