class Solution(object):
    def canMakePaliQueries(self, s, queries):
        """
        :type s: str
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        alphabet = set(s)
        dic = dict()
        for char in alphabet:
            dic[char] = [0 for _ in range(len(s))]
        
        for i, ch in enumerate(s):
            for char in alphabet:
                if ch == char:
                    if i > 0:
                        dic[ch][i] = dic[ch][i - 1] + 1
                    else:
                        dic[ch][i] = 1
                else:
                    if i > 0:
                        dic[char][i] = dic[char][i - 1] 
        res = []
        for left, right, k in queries:
            odd_cnt = 0
            for char in alphabet:
                # print char, dic[char], left, right
                if left > 0:
                    if (dic[char][right] - dic[char][left - 1]) % 2 == 1:
                        odd_cnt += 1
                else:
                    if dic[char][right] % 2 == 1:
                        odd_cnt += 1
            if odd_cnt // 2 <= k:
                res.append(True)
            else:
                res.append(False)                
        return res
    
