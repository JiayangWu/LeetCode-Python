class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        record = ["1"]
        for i in range(1, n):
            pre = record[i - 1]
            idx = 0
            tmp = ""
            while idx < len(pre):
                cnt = 1
                while(idx + 1 < len(pre) and pre[idx] == pre[idx + 1]):
                    idx += 1
                    cnt += 1
                tmp += str(cnt) + pre[idx]
                idx += 1
            record.append(tmp)
        return record[-1]