class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        p = [[score[i], i] for i in range(len(score))]

        p.sort(key = lambda x: -x[0])

        res = [0 for _ in score]
        for index, pair in enumerate(p):
            score, original_index = pair[0], pair[1]

            if index == 0:
                val = "Gold Medal"
            elif index == 1:
                val = "Silver Medal"
            elif index == 2:
                val = "Bronze Medal"
            else:
                val = str(index + 1)

            res[original_index] = val
        return res