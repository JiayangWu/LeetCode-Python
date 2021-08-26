class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        people.sort()
        left, right = 0, len(people) - 1
        boat_count = 0
        while left <= right:
            # print (people[left], people[right], boat_count)
            if people[left] + people[right] <= limit:
                left += 1
                right -= 1
            else:
                right -= 1
            boat_count += 1
        return boat_count
