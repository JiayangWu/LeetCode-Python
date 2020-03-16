class Solution(object):
    def compressString(self, S):
        """
        :type S: str
        :rtype: str
        """
        pre = None
        cnt = 0
        res = ""
        for ch in S:
            if not pre:
                cnt += 1
                pre = ch 
            else:
                if ch == pre:
                    cnt += 1
                else:
                    res += pre + str(cnt)
                    cnt = 1
                    pre = ch
        if S:
            res += pre + str(cnt)
        return res if len(res) < len(S) else S