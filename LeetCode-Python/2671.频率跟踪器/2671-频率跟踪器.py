from collections import defaultdict
class FrequencyTracker:

    def __init__(self):
        self.freq2num = defaultdict(set)
        self.num2freq = defaultdict(int)

    def add(self, number: int) -> None:
        # print(self.num2freq, self.freq2num)
        freq = self.num2freq[number]
        self.num2freq[number] += 1
        if number in self.freq2num[freq]:
            self.freq2num[freq].remove(number)
        self.freq2num[freq + 1].add(number)

    def deleteOne(self, number: int) -> None:
        # print(self.num2freq, self.freq2num)
        if number not in self.num2freq or self.num2freq[number] == 0:
            return
        freq = self.num2freq[number]
        self.num2freq[number] -= 1
        if number in self.freq2num[freq]:
            self.freq2num[freq].remove(number)
        self.freq2num[freq - 1].add(number)

    def hasFrequency(self, frequency: int) -> bool:
        return len(self.freq2num[frequency]) > 0


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)