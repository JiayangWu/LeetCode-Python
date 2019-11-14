class Solution(object):
    def minAvailableDuration(self, slots1, slots2, duration):
        """
        :type slots1: List[List[int]]
        :type slots2: List[List[int]]
        :type duration: int
        :rtype: List[int]
        """
        slots1 = sorted(slots1, key = lambda x:x[0])
        slots2 = sorted(slots2, key = lambda x:x[0])
        slots = []
        i, j = 0, 0
        while i < len(slots1) and j < len(slots2):
            if slots1[i][1] < slots2[j][0]:
                i += 1
                continue
            elif slots1[i][0] > slots2[j][1]:
                j += 1
                continue
            start = max(slots1[i][0], slots2[j][0])
            end = min(slots1[i][1], slots2[j][1])
            slots.append([start, end])
            i += 1
                
        print(slots)
        for start, end in slots:
            if end - start >= duration:
                return [start, start + duration]
        return []
        
        
