class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        small, equal, larger = [], 0, []

        for num in nums:
            if num < pivot:
                small.append(num)
            elif num == pivot:
                equal += 1
            else:
                larger.append(num)
        
        return small + equal * [pivot] + larger