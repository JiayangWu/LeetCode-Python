class Solution:
    def countSeniors(self, details: List[str]) -> int:
        # res = 0
        # for detail in details:
        #     if int(detail[-4:-2]) > 60:
        #         res += 1
        # return res
        return sum([int(detail[-4:-2]) > 60 for detail in details])