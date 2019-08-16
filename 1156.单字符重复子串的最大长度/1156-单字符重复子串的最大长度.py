class Solution(object):
    def maxRepOpt1(self, text):
        """
        :type text: str
        :rtype: int
        """
        if len(text) == text.count(text[0]):
            return len(text)
        record = collections.Counter(text)
        start, end = 0, 1
        cur, nxt, idx_nxt = text[0], None, 0
        res = 1
        while end < len(text):           
            if text[end] != cur :
                if nxt is None:
                    nxt = text[end] #找到了第一个异字符
                    idx_nxt = end
                else: #当前段已经完成
                    l = end - 1 - start + 1 #计算包括一个异字符的同字符子串长度
                    if l <= record[text[start]]: #有多的同字符可以把这个夹在中间的同字符换掉
                        res = max(res, l)
                    else:
                        res = max(res, l - 1) #只能用目前字串的边界同字符跟异字符交换

                    cur = nxt
                    nxt = None
                    start, end = idx_nxt, idx_nxt
                    idx_nxt = 0
            if end == len(text) - 1: #到输入终点了
                # print end
                l = end  - start + 1 #计算包括一个异字符的同字符子串长度
                # print l
                if l <= record[text[start]]: #有多的同字符可以把这个夹在中间的同字符换掉
                    res = max(res, l)
                else:
                    res = max(res, l - 1) #只能用目前字串的边界同字符跟异字符交换
                
            # print text[start:end + 1]
            end += 1
            # print end
        return res