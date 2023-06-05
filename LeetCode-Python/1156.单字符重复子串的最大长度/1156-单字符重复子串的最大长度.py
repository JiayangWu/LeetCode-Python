class Solution:
    def maxRepOpt1(self, text: str) -> int:
        c = Counter(text)
        res = 0
        for i in range(len(text)):
            j = i + 1
            while j < len(text) and text[j] == text[i]:
                j += 1
            
            # [i, j)
            cnt = j - i
            if i > 0 and j < len(text) and cnt < c[text[i]]:
                res = max(res, cnt + 1)
            
            k = j + 1
            while k < len(text) and text[k] == text[i]:
                k += 1
            # [i, j)[j + 1, k) swap text[j] if possible
            res = max(res, min(k - i, c[text[i]]))
            i = j
        return res