class Solution:
    def maximumTastiness(self, price: List[int], k: int) -> int:
        # 13, 1, 21 - 12, 20, 8
        price = set(price)
        if len(price) < k:
            return 0

        # 1, 2, 5, 8, 13, 21
        price = sorted(list(price))
        left, right = 0, price[-1] - price[0]
        while left <= right:
            mid = (left + right) // 2 # target tastyness

            cnt, prev = 1, price[0]
            for p in price:
                if prev + mid <= p: # 又找到了一个
                    cnt += 1
                    prev = p
            
            if cnt >= k:
                left = mid + 1
            elif cnt < k:
                right = mid - 1
        
        return right