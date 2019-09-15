class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        dic = collections.Counter(text)
        #balloon
        min_count = 99999999
        for char in "balon":
            tmp = dic[char]
            if char in "lo":
                tmp /= 2
            min_count = min(min_count, tmp)
        return min_count