from heapq import *
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        
        dic = Counter(nums)
        bucket = [[] for _ in range(len(nums) + 1)]
        for num, fre in dic.items():
            bucket[fre].append(num)
        # print (bucket)

        res = []
        for i in range(len(bucket) - 1, -1, -1):
            if bucket[i]:
                if len(bucket[i]) <= k - len(res):
                    res += bucket[i]
                else:
                    res += bucket[i][:k - len(res)]
                    break
        return res
