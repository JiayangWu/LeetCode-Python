class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if len(num1) < len(num2):
            num1, num2 = num2, num1
        if num1 == "0" or num2 == "0":
            return "0"
        
        num2 = num2[::-1]
        tmp, res = [],[]
        for i, char in enumerate(num2):
            tmp = self.stringMultiDigit(num1, int(char)) + "0" * i #计算当前位乘法的结果，注意末尾添0
            res = self.stringPlusString(res, tmp) #加上当前位结果
            
        return "".join(res)
    
    def stringMultiDigit(self,s, n): #计算一个字符串和一个数字的乘积， 返回字符串
        s = s[::-1]
        l = []
        for char in s:
            l.append(int(char))
            
        for i, char in enumerate(l):
            l[i] *= n
            
        for i, char in enumerate(l):
            while(l[i] > 9):
                tmp = l[i] // 10
                l[i] -= tmp * 10
                if i == len(l) - 1:
                    l.append(0)
                l[i + 1] +=  tmp
                
        return "".join(str(char) for char in l[::-1])
            
        
    def stringPlusString(self,s1, s2): #字符串加法，返回字符串
        # print s1, s2
        s1, s2 = s1[::-1], s2[::-1]
        l1, l2 = [], []
        for char in s1:
            l1.append(int(char))
        for char in s2:
            l2.append(int(char))
        # tmp = []
        if len(l1) < len(l2):
            l1, l2 = l2, l1
        i = 0
        for i in range(len(l2)):
            l1[i] += l2[i]
            if l1[i] > 9:
                l1[i] -= 10
                if i == len(l1) - 1:
                    l1.append(0)
                l1[i + 1] += 1
        i += 1
        if i < len(l1) - 1: #处理最后一位可能的进位
            if l1[i] > 9:
                l1[i] -= 10
                if i == len(l1) - 1:
                    l1.append(0)
                l1[i + 1] += 1

        return "".join(str(char) for char in l1[::-1])
    