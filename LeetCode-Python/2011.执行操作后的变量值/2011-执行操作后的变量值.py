class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        res = 0
        for operation in operations:
            if operation[0] == "-" or operation[-1] == "-":
                res-= 1
            else:
                res += 1

        return res