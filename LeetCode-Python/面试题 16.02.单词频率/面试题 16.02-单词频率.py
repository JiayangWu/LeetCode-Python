from collections import Counter
class WordsFrequency:

    def __init__(self, book: List[str]):
        self.word2freq = Counter(book)

    def get(self, word: str) -> int:
        return self.word2freq[word]



# Your WordsFrequency object will be instantiated and called as such:
# obj = WordsFrequency(book)
# param_1 = obj.get(word)