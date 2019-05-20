class Solution(object):
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        s = [0 for i in seats]
        
        #正着扫一遍再反着扫一遍
        for i, seat in enumerate(seats):
            if seat == 1:
                seat_index = i
                
        for index, seat in enumerate(seats):
            if seat == 1:
                s[index] = -1
                seat_index = index
            else:
                s[index] = abs(index - seat_index)
        # print s
        for i in range(len(seats) - 1, - 1, -1):
            if seats[i] == 1:
                seat_index = i
                break

        for i in range(len(seats) - 1, - 1, -1):
            if seats[i] == 1:
                seat_index = i
            else:
                # print seat_index - i
                s[i] =  min(s[i], abs(seat_index - i))

        return max(s)