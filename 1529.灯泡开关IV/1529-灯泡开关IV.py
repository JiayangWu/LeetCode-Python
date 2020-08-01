class Solution(object):
    def minFlips(self, target):
        """
        :type target: str
        :rtype: int
        """
        i = 0
        flag = 0 
        pre = None
        res = 0
        for i, ch in enumerate(target):
            if not flag and ch == "0":
                continue 
            else:
                if ch != pre:
                    res += 1
                flag = 1
                pre = ch 
        return res