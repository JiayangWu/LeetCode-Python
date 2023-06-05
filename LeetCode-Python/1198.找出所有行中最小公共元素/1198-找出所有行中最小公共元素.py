class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        for candidate in mat[0]:
            all_found_candidate = True
            for row in mat[1:]:
                found_candidate = False
                left, right = 0, n - 1
                while left <= right:
                    mid = (left + right) // 2
                    if row[mid] == candidate:
                        found_candidate = True
                        break
                    elif row[mid] < candidate:
                        left = mid + 1
                    else:
                        right = mid - 1
            
                if not found_candidate:
                    all_found_candidate = False
                    break
            if all_found_candidate:
                return candidate 
        return -1
                