class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        ones = []
        for index, box in enumerate(boxes):
            if box == "1":
                ones.append(index)

        res = []
        for index, box in enumerate(boxes):
            cur_sum = 0
            for one_index in ones:
                cur_sum += abs(one_index - index)
            res.append(cur_sum)

        return res
