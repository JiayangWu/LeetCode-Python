class Solution(object):
    def isOneEditDistance(self, s, t):      
        distance = len(s) - len(t)
        if abs(distance) > 1: #长度都差了不止一位，肯定不对
            return False
        if not s or not t: #两者有一个为空返回真，两个都为空返回假
            return s != t
        
        edit = 0 #代表编辑次数
        i, j = 0, 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]: #无需编辑
                i += 1 #两个指针都顺序后延一位
                j += 1
            else:
                if edit: #唯一的机会已经用完了
                    return False
                if distance == 1: #删除
                    i += 1
                elif distance == -1:#插入
                    j += 1
                else: #替换
                    i += 1
                    j += 1
                edit += 1

        if i < len(s): #如果t没了，s还多了一位，取决于edit还是不是0
            return edit == 0
        if j < len(t): #如果s没了，t还多了一位，取决于edit还是不是0
            return edit == 0
        
        return i == len(s) and j == len(t) and edit == 1 