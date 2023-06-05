class Solution:
    def maximizeSweetness(self, sweetness: List[int], k: int) -> int:
        left, right = 0, sum(sweetness) 
        k += 1
        while left <= right:
            mid = (left + right) // 2 # mid 是每一块巧克力的甜度下限而不是上限，也是返回的值
            pieces_cnt, cur_sum = 0, 0
            for s in sweetness:
                if cur_sum + s >= mid:
                    pieces_cnt += 1
                    cur_sum = 0
                else:
                    cur_sum += s
            
            if pieces_cnt < k: # 需要切更多块
                right = mid - 1
            elif pieces_cnt == k:
                left = mid + 1
            elif pieces_cnt > k:
                left = mid + 1
        return right