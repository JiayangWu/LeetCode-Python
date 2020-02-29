class ProductOfNumbers(object):

    def __init__(self):
        self.prefix = [1]

    def add(self, num):
        """
        :type num: int
        :rtype: None
        """
        if num:
            self.prefix.append(self.prefix[-1] * num)
        else:
            self.prefix = [1]

    def getProduct(self, k):
        """
        :type k: int
        :rtype: int
        """
        if k >= len(self.prefix):
            return 0
        return self.prefix[-1] / self.prefix[-k - 1]