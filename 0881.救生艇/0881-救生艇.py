class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        people.sort()
        left, right = 0, len(people) - 1
        res = 0
        while left <= right:
            if left == right:
                res += 1
                break
            if people[left] + people[right] <= limit:
                left += 1
                right -= 1
                res += 1
            else:
                right -= 1
                res += 1
        return res 