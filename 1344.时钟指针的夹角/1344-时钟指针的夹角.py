class Solution(object):
    def angleClock(self, hour, minutes):
        """
        :type hour: int
        :type minutes: int
        :rtype: float
        """
        min_angle = minutes * 1.0 / 60 * 360
        hour_angle = hour * 1.0 / 12 * 360 + minutes * 1.0 / 60 * 30

        res = abs(hour_angle - min_angle)

        return res if res < 180 else 360 - res