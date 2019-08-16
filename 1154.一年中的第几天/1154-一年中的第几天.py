class Solution(object):
    def dayOfYear(self, date):
        """
        :type date: str
        :rtype: int
        """
        days1 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        days2 = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        
        Date = date.split("-")
        year, month, day = int(Date[0]), int(Date[1]), int(Date[2])

        if not year % 400 or (not year % 4 and year % 100):
            return sum(days2[:month - 1]) + day
        return sum(days1[:month - 1]) + day
