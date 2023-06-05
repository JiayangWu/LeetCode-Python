class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        # words = words.lower()
        g1 = ["q","w","e","r","t","y","u","i","o","p"]
        g2 = ["a","s","d","f","g","h","j","k","l"]
        g3 = ["z","x","c","v","b","n","m"]
        res = list()
        for word in words:
            temp = word.lower()
            if temp[0] in g1:
                flag = 1
            elif temp[0] in g2:
                flag = 2
            elif temp[0] in g3:
                flag = 3
            temp = set(temp)
            for char in temp:
                if flag == 1 and char not in g1:
                    flag = 0
                    break
                if flag == 2 and char not in g2:
                    flag = 0
                    break
                if flag == 3 and char not in g3:
                    flag = 0
                    break
            if flag:
                res.append(word)
                
        return res