class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        from collections import defaultdict
        dic = defaultdict(int)

        for pair in cpdomains:
            splitted_pair = pair.split()
            cnt, domain = splitted_pair[0], splitted_pair[1]
            cnt = int(cnt)

            for i in range(len(domain)):
                if not i or domain[i] == ".":
                    dic[domain[i:].lstrip(".")] += cnt

        res = []
        for domain, frequency in dic.items():
            res.append(" ".join([str(frequency), domain]))
        return res