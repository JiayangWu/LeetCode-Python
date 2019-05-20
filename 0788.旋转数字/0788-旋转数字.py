class Solution(object):
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        valid = [2, 5, 6, 9]
        same = [0, 1, 8]
        res = 0
        
        for i in range(1, N + 1):
            t = i
            flag = 1
            while(t):
                temp = t % 10
                if temp not in same:
                    flag = 0
                    break
                t /= 10
            if flag:
                continue
              
            t = i
            flag = 1
            while(t):
                temp = t % 10
                if temp not in valid and temp not in same:
                    flag = 0
                    break
                t /= 10
            if flag:
                # print i
                res += 1
                
        return res