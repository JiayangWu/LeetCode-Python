class Solution(object):
    def longestWPI(self, hours):
        """
        :type hours: List[int]
        :rtype: int
        """
        n = len(hours)
        a = [0]*n
        for i,hour in enumerate(hours):
            if hour>8:
                a[i]=1
            else:
                a[i]=-1
        for i in range(1,n):
            a[i]+=a[i-1]
        b={}
        res = 0
        for i in range(n):
            if a[i]>0:
                res = max(res,i+1)
            else:
                if a[i]-1 in b:
                    res = max(res,i-b[a[i]-1])
                if a[i] not in b:
                    b[a[i]]=i
        return res
            