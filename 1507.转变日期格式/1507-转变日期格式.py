class Solution(object):
    def reformatDate(self, date):
        """
        :type date: str
        :rtype: str
        """
        date = date.split(" ")
        
        day = "0" + date[0][:1] if len(date[0]) == 3 else date[0][:2]
        mon = {"Jan":"01", "Feb":"02", "Mar":"03", "Apr":"04", "May":"05", "Jun":"06",
               "Jul":"07", "Aug":"08", "Sep":"09", "Oct":"10", "Nov":"11", "Dec":"12"}[date[1]]
        year = date[2]
        return "-".join([year, mon, day])