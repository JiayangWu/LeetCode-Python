class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        resList = []
        resMap = {}
        for s in cpdomains:
            count, domains = s.split(' ')
            n = domains.count('.')
            tmp = domains
            for i in range(n+1):
                if resMap.has_key(tmp):
                    resMap[tmp] = resMap[tmp] + int(count)
                else:
                    resMap[tmp] = int(count)
                index = tmp.find('.') + 1
                if index == -1:
                    break
                else:
                    tmp = tmp[index:]
        # for key, value in resMap.items():
        #     resList.append(str(value) + ' ' + key);
        # return resList
        return [str(resMap[key]) + ' ' + key for key in resMap]