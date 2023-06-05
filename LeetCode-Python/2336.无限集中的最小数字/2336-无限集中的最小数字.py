from heapq import *
class SmallestInfiniteSet:

    def __init__(self):
        self.min_heap = [i for i in range(1, 1001)]
        heapify(self.min_heap)
        self.set = set(self.min_heap)

    def popSmallest(self) -> int:
        val = heappop(self.min_heap)
        self.set.remove(val)
        return val

    def addBack(self, num: int) -> None:
        if num not in self.set:
            heappush(self.min_heap, num)
            self.set.add(num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)