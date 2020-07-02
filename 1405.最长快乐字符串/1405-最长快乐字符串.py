class Solution(object):
    def longestDiverseString(self, a, b, c):
        """
        :type a: int
        :type b: int
        :type c: int
        :rtype: str
        """
        from heapq import *
        heap = []
        res = ""
        if a:
            heappush(heap, (-a, "a"))
        if b:
            heappush(heap, (-b, "b"))
        if c:
            heappush(heap, (-c, "c"))
        pre_cnt, pre_char = None, None
        s = a + b + c

        while heap:
            cnt, char = heappop(heap)
            cnt = -cnt
            # print cnt, char

            if cnt > s - cnt:
                res += char * min(cnt, 2)
                cnt -= min(cnt, 2)
                s -= min(cnt, 2)
            else:
                res += char 
                cnt -= 1
                s -= 1

            if pre_cnt:
                heappush(heap, (-pre_cnt, pre_char))
            pre_cnt, pre_char = cnt, char
        return res