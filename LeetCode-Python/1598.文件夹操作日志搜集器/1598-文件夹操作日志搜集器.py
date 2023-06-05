class Solution:
    def minOperations(self, logs: List[str]) -> int:
        dir_count = 0
        for log in logs:
            if log == "../":
                if dir_count > 0:
                    dir_count -= 1
            elif log != "./":
                dir_count += 1
        return dir_count