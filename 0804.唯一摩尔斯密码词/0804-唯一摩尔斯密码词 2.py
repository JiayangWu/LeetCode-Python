class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        moore = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        queue = set()
       
        for word in words:
            temp = ""
            for char in word:
                temp += moore[ord(str(char)) - ord("a")]
            queue.add(temp)
        
        return len(queue)