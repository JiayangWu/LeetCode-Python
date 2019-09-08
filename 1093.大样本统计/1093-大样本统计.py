class Solution(object):
    def sampleStats(self, count):
        """
        :type count: List[int]
        :rtype: List[float]
        """
        s = 0
        total_cnt = sum(count)
        cnt  = 0
        avg, median, mean, mean_cnt = 0, 0, 0, 0
        min_element, max_element = 0, 0
        #找最小值
        for i in range(len(count)):
            if count[i] != 0:
                min_element = i
                break
        #找最大值
        for i in range(len(count) - 1, -1, -1):
            if count[i] != 0:
                max_element = i
                break
                
        #找一共统计了多少个数字        
        geshu = 0
        for i in count:
            if i > 0:
                geshu += i
                
        find = False
        for i, num in enumerate(count):
            s += num * i #计算总和
            if mean_cnt < num: #找count数组最大值的下标
                mean = i
                mean_cnt = num
                
            cnt += num #找目前出现了多少个数字
            if cnt > total_cnt // 2 and find == False: 
                if total_cnt % 2: #中位数肯定是一个数
                    median = i
                    find = True
                else:
                    if cnt - num == total_cnt // 2: #中位数有两个不同的数
                        for j in range(i - 1, -1, -1): #往前找上一个数
                            if count[j] > 0:
                                median = (i + j) /2.0
                                find = True
                                break
                    else:#中位数有两个相同的数
                        median = i
                        find = True
                                
        return [min_element, max_element, 1.0 * s /geshu, median, mean ]
                                
                                
            