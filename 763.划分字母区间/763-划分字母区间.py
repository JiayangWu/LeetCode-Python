class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        from collections import defaultdict
        dic = defaultdict(list)

        for ch in "abcdefghijklmnopqrstuvwxyz":
            for i, char in enumerate(S):
                if char == ch:
                    dic[ch].append(i)
                    break

            for i in range(len(S) - 1, -1, -1):
                if S[i] == ch:
                    dic[ch].append(i)
                    break


        intervals = []
        for val in dic.values():
            intervals.append(val)
        
        intervals.sort()
        #print intervals

        res = []
        start, end = 0, 0
        for s, e in intervals:
            if s > end:
                res.append(end - start + 1)
                start, end = s, e
            else:
                end = max(e, end)
        res.append(end - start + 1)

        return res