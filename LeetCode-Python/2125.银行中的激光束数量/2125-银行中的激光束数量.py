class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        res = 0
        last_device_count = 0
        for row_index, row in enumerate(bank):
            cur_device_count = row.count("1")
            res += cur_device_count * last_device_count
            if cur_device_count:
                last_device_count = cur_device_count
        return res