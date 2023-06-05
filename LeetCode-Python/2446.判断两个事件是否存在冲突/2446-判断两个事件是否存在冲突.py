class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        return not (self.time1EarlierThanTime2(event1[1], event2[0]) or self.time1EarlierThanTime2(event2[1], event1[0]))

    def time1EarlierThanTime2(self, time1, time2):
        h1, h2 = int(time1[:2]), int(time2[:2])
        m1, m2 = int(time1[3:]), int(time2[3:])
        return h1 < h2  or (h1 == h2 and m1 < m2)