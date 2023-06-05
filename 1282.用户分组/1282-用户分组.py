class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        from collections import defaultdict

        size2people = defaultdict(list)
        for i, size in enumerate(groupSizes):
            size2people[size].append(i)

        res = []
        for size, peoples in size2people.items():
            for i in range(0, len(peoples), size):
                res.append(peoples[i: i + size])
        return res