class Solution(object):
    def shortestWay(self, source, target):
        """
        :type source: str
        :type target: str
        :rtype: int
        """

        import collections
        dicse = collections.Counter(source)
        dictt = collections.Counter(target)

        for key, val in dictt.items():
            if dicse.get(key, 0) == 0:
                return -1

        cnt = 0
        start, end = 0, 0
        i = 0
        while(i < len(target)):
            char = target[i]
            while(source[start] != char): #找起点，一定能找到
                start += 1
            end = start + 1

            i += 1
            while(i < len(target) and end < len(source)):
                if source[end] == target[i]: #找最长的子序列
                    i += 1
                end += 1

            cnt += 1
            start = 0 #重置起点，为下一轮做准备
            
        return cnt

            