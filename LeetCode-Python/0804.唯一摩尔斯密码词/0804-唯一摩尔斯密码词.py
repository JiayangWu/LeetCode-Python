class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        res = set()
        mores = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

        for word in words:
            word_mores = ""
            for char in word:
                word_mores += mores[ord(char) - ord("a")]
            res.add(word_mores)
        return len(res)