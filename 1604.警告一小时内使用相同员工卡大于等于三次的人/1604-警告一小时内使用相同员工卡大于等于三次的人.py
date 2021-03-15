class Solution(object):
    def alertNames(self, keyName, keyTime):
        """
        :type keyName: List[str]
        :type keyTime: List[str]
        :rtype: List[str]
        """
        from collections import defaultdict
        name2time = defaultdict(list)

        res = set()
        
        def timeToMinutes(time):
            # convert 10:05 to 605
            splitted_time = time.split(":")
            return 60 * int(splitted_time[0]) + int(splitted_time[1])

        pairs = sorted(zip(keyName, keyTime), key = lambda x: (x[0], x[1]))

        for name, time in pairs:
            if name not in res:
                name2time[name].append(time)
                if len(name2time[name]) >= 3 and 0 <= timeToMinutes(time) - timeToMinutes(name2time[name][-3]) <= 60:
                    res.add(name)
            
        return sorted(list(res))

        
