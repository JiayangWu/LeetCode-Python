class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left, right = max(weights), sum(weights)
        while left <= right:
            mid = (left + right) // 2 # answer to be returned, max(capacity)

            capacity = mid
            needed_days, cur_sum = 1, 0
            for w in weights:
                if cur_sum + w > capacity:
                    needed_days += 1
                    cur_sum = w
                else:
                    cur_sum += w
            # print(capacity, needed_days, days)
            if needed_days > days: # need to increase the capacity
                left = mid + 1
            elif needed_days == days:
                right = mid - 1
            elif needed_days < days:
                right = mid - 1
        return left