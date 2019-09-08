class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        #第一行和最后一行都是相差 2 * (n - 1)
        #对于直角在上面的直角三角形， 相差 2 * (n - 1 - i)
        #对于直角在下面的直角三角形， 相差 2 * i
        if not s or numRows == 1:
            return s
        res = ""
        for idx in range(numRows):
            if idx < len(s):
                res += s[idx]
            
            if idx in [0, numRows - 1]:
                tmp = idx + 2 *(numRows - 1)
                while tmp < len(s):
                    res += s[tmp]
                    tmp += 2 *(numRows - 1)
            else:
                tmp = idx + 2 * (numRows - 1 - idx)
                tri = "down"
                while tmp < len(s):
                    res += s[tmp]
                    if tri == "up":
                        tmp += 2 * (numRows - 1 - idx)
                        tri = "down"
                    else:       
                        tmp += 2 * idx
                        tri = "up"
                    
        return res
                    
            
                    
            
            