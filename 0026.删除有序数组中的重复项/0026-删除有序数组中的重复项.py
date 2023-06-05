class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        visited = set()
        index = 0
        for num in nums:
            if num not in visited:
                visited.add(num)
                nums[index] = num
                index += 1
        return index