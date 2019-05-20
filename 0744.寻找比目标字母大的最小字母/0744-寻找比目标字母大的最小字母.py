class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        for i in range(len(letters)):
            if target < letters[i]:
                return letters[i]
            if target >= letters[-1]:
                return letters[0]