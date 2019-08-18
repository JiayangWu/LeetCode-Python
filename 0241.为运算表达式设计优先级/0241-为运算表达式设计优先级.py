class Solution(object):
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        self.record = collections.defaultdict(list)
        self.work(input)
        return self.record[input]
        
        
        
    def work(self, input):
        if not input:
            return []
        if input in self.record:
            return self.record[input]
        
        if input.isdigit():
            self.record[input] = [int(input)]
            return self.record[input]
        res = []
        
        for i in range(len(input)):
            if input[i] in "+-*":
                left = self.diffWaysToCompute(input[:i])
                right = self.diffWaysToCompute(input[i + 1:])
                
                for l in left:
                    for r in right:
                        if input[i] == "+":
                            res.append(l + r)
                        elif input[i] == "-":
                            res.append(l - r)
                        else:
                            res.append(l * r)
                            
        self.record[input] = res
        return self.record[input]