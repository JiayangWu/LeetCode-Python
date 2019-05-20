class Solution(object):
    def convert(self, s, n):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        #ур╧Фби
        if n <= 1:
            return s
        l = len(s)
        res = ""
        for i in range(n):
            tmp, index = "", i
            if i in [0, n - 1]:
                while(index < l):
                    
                    tmp += s[index]
                    index += 2 * (n - 1)
            else:
                state = "down"
                while(index < l):
                    tmp += s[index]
                    if state == "down":
                        state = "up"
                        index += 2 * (n - 1 - i)
                    else:
                        state = "down"
                        index += 2 * i
            res += tmp

        return res
                    
                        
            