class MRUQueue:

    def __init__(self, n: int):
        self.queue = [i for i in range(1, n + 1)]

    def fetch(self, k: int) -> int:
        node = self.queue[k - 1]
        self.queue = self.queue[:k - 1] + self.queue[k:] + [node]
        return node



# Your MRUQueue object will be instantiated and called as such:
# obj = MRUQueue(n)
# param_1 = obj.fetch(k)