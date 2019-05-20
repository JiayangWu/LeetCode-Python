class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        flag = 0
        if x < 0:
            flag = 1
        if flag:
            s = str(x)[1:]
            s = s[::-1]
            x = -1 *int(s)            
        else:
            s = str(x)
            s = s[::-1]
            x = int(s)
            
        if x < -1 * 2 **31 or x > 2** 31 -1:
            return 0    
        return x