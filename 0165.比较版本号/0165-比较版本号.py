class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        l1 = version1.split(".")
        l2 = version2.split(".")
        
        i, j = 0, 0
        while i < len(l1) and j < len(l2): # 逐位比大小
            num1, num2 = int(l1[i]), int(l2[j])
            if num1 < num2:
                return -1
            elif num1 > num2:
                return 1
            i += 1
            j += 1

        if len(l1) == len(l2) and num1 == num2: #长度相等而且最后一位也相等
            return 0

        if len(l1) > len(l2): #如果l1还在而l2结束了
            while i < len(l1) and int(l1[i]) == 0:  #判断l1后面是不是全是0
                i += 1
            if i == len(l1): #如果全是0，则还相等
                return 0
            else:
                return 1
            
        if len(l2) > len(l1):
            while j < len(l2) and int(l2[j]) == 0: #判断l2后面是不是全是0
                j += 1
            if j == len(l2): #如果全是0，则还相等
                return 0
            else:
                return -1
            return -1