class Solution(object):
    def carPooling(self, trips, capacity):
        """
        :type trips: List[List[int]]
        :type capacity: int
        :rtype: bool
        """
        time = [0 for _ in range(1005)]
        
        for num, start, end in trips:
            time[start] += num
            time[end] -= num
            
        for i, x in enumerate(time):
            time[i] += time[i - 1]
            if time[i] > capacity:
                return False
            
        return True
        