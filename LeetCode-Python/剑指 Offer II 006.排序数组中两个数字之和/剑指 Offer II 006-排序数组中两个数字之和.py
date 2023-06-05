class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        num2index = dict()
        for index, num in enumerate(numbers):
            if target - num in num2index:
                return [num2index[target - num], index]
            num2index[num] = index