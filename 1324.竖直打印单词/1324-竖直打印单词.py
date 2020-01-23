class Solution(object):
    def printVertically(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
       
        l = s.split(" ")
        max_l = max([len(item) for item in l])
        
        res = [""] * max_l
        for i in range(max_l):
            tmp = ""
            for j in range(len(l)):
                if len(l[j]) > i:
                    tmp += l[j][i]
                else:
                    tmp += " "
            res[i] = tmp.rstrip()
            
        return res
        # l = s.split(" ")
        # res = []
        # for item in zip(*l):
        #     res.append("".join(item))
        # return res