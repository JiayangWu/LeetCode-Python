class Solution(object):
    def corpFlightBookings(self, bookings, n):
        """
        :type bookings: List[List[int]]
        :type n: int
        :rtype: List[int]
        """
        f = [0 for _ in range(n + 1)]
        
        for i, j, k in bookings:
            f[i - 1] += k
            f[j] -= k
        # print f    
        for i in range(1, n + 1):
            f[i] += f[i - 1]
        # print f
        return f[:-1]