# -*- coding: utf-8 -*-
class Solution(object):
    def minAddToMakeValid(self, S):
        """
        :type S: str
        :rtype: int
        """
        dic = {"(":"", ")" : "("}
        res = len(S)
        temp = [None]
        for item in S:
            # print item
            if temp[-1] != dic[item.encode('utf-8')]:
                temp.append(item)
            else:
                temp = temp[:-1]
        return len(temp) -1
            
        