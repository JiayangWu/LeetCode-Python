class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        res = set()
        for email in emails:
            local, domain = email.split("@")
            local = local[:local.find('+')].replace(".","")
            res.add(local + "@" + domain)
        # print res
        return len(res)