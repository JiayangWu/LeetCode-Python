class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        # l = [1,2,3,4,5,6]
        # for i in range(len(l)):
        #     for j in range(i + 1, len(l)):
        #         for k in range(j + 1, len(l)):
        #             print (l[i], l[j], l[k])
        from collections import defaultdict
        max_visit_cnt = 0
        max_visit_websites = []
        name2web = defaultdict(list)
        web2freq = defaultdict(int)
        comb = []
        for i in range(len(username)):
            comb.append((username[i], timestamp[i], website[i]))
        comb.sort(key = lambda x:x[1])
        for i in range(len(username)):
            name2web[comb[i][0]].append(comb[i][2])
        
        for name, webs in name2web.items():
            visited = set()
            for i in range(len(webs)):
                for j in range(i + 1, len(webs)):
                    for k in range(j + 1, len(webs)):
                        tmp = ",".join([webs[i], webs[j], webs[k]])
                        if tmp in visited:
                            continue
                        visited.add(tmp)
                        web2freq[tmp] += 1

                        if web2freq[tmp] > max_visit_cnt:
                            max_visit_cnt = web2freq[tmp]
                            max_visit_websites = [tmp]
                        elif web2freq[tmp] == max_visit_cnt:
                            max_visit_websites.append(tmp)
        # print (max_visit_websites)
        max_visit_websites.sort()
        # print (max_visit_websites)
        s = max_visit_websites[0]
        l = s.split(",")
        return l

