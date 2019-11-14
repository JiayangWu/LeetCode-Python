class Solution(object):
    def numMatchingSubseq(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """
        from collections import defaultdict
        
        dic = defaultdict(list)
        for i, ch in enumerate(S):
            dic[ch].append(i)
            
        res = 0
        for word in words:
            pre = -1
            flag = True
            for i, ch in enumerate(word):
                l = dic[ch]
                # 在l找第一个比pre大的元素
                idx = bisect.bisect(l, pre)
                
                if idx == len(l):# 没找到
                    flag = False
                    break
                pre = l[idx]
                
            if flag:
                res += 1

        return res