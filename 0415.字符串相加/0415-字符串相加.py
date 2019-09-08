class Solution(object):
    def addStrings(self, s1, s2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        l1, l2 = len(s1), len(s2)
        if l1 < l2:
            s1, s2 = s2, s1
            l1, l2 = l2, l1
        s1 = [int(x) for x in s1]
        s2 = [int(x) for x in s2]
        s1, s2 = s1[::-1], s2[::-1]
        for i, digit in enumerate(s2):
            s1[i] += s2[i]
            
        s1 = self.CarrySolver(s1)
        s1 = s1[::-1]
        return "".join(str(x) for x in s1)
    
    def CarrySolver(self, nums):  
        #这个函数的功能是：将输入的数组中的每一位处理好进位
        #举例：输入[15, 27, 12], 返回[5, 8, 4, 1]
        i = 0
        while i < len(nums):
            if nums[i] >= 10:
                carrier = nums[i] // 10
                if i == len(nums) - 1:
                    nums.append(carrier)
                else:
                    nums[i + 1] += carrier
                nums[i] %= 10
            i += 1
                    
        return nums