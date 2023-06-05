class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        candy_to_be_distributed = 1
        child = 1
        res = [0] * (num_people + 1)
        while candies:
            give = min(candy_to_be_distributed, candies)
            candies -= give
            res[child] += give
            candy_to_be_distributed += 1
            child += 1
            if (child > num_people):
                child = 1
        return res[1:]