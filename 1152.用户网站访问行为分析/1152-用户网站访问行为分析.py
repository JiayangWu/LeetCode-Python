class Solution(object):
    def mostVisitedPattern(self, username, timestamp, website):
        """
        :type username: List[str]
        :type timestamp: List[int]
        :type website: List[str]
        :rtype: List[str]
        """
        from collections import defaultdict
        record = defaultdict(list)
        for i, un in enumerate(username):
            record[un].append([timestamp[i], website[i]])
        # print record
        row = defaultdict(int)
        for key in record.keys():
            record[key].sort()
            # print record[key]
            used = set()
            for i in range(len(record[key])):
                for j in range(i + 1, len(record[key])):
                    for k in range(j + 1, len(record[key])):
                        sequence = record[key][i][1] + "+" + record[key][j][1]+ "+" + record[key][k][1]
                        if sequence not in used:
                            row[sequence] += 1
                            used.add(sequence)
        # print row
        possible_sol = []
        max_freq = max(row.values())
        for key, val in row.items():
            if val == max_freq:
                possible_sol.append(key.split("+"))
        possible_sol = possible_sol[::-1]
        # print possible_sol
        if len(possible_sol) > 1:
            possible_sol.sort()
        return possible_sol[0]