class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos, neg = [], []

        for num in nums:
            if num > 0:
                pos.append(num)
            else:
                neg.append(num)

        t = [(pos[i], neg[i]) for i in range(len(pos))]
        
        res = []
        for pair in t:
            res.append(pair[0])
            res.append(pair[1])
        return res