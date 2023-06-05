class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        from collections import defaultdict
        table_set = set()
        tablefood2cnt = defaultdict(int)
        food_set = set()

        for order in orders:
            table, food = order[1], order[2]
            food_set.add(food)
            table_set.add(table)
            tablefood2cnt[table + "-" + food] += 1

        sorted_table = sorted(list(table_set), key = lambda x: int(x))
        sorted_food = sorted(list(food_set))
        res = [["Table"] + sorted_food]

        for table in sorted_table:
            temp = [table]
            for f in sorted_food:
                temp.append(str(tablefood2cnt[table + "-" + f]))
            res.append(temp)
        return res