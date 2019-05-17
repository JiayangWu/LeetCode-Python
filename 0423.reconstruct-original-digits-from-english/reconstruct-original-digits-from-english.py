class Solution(object):
    def originalDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        # zero one   two three  four    five   six seven       eight nine 
        # z   o（先2  w  r(先4)  u      f(先4)  x  s（先6）    t(先3) 最后看e
        #所以一个可行的查找的顺序是 two, four, six, one, three, five, seven, eight, nine
        order = ["zero", "two", "four", "six", "one", "three", "five", "seven", "eight", "nine"]
        find =  ["z", "w",    "u",   "x",    "o",  "r",     "f",    "v",     "t",     "e"]
        digit = [0, 2, 4, 6, 1, 3, 5, 7, 8, 9]
        
        record = [0 for _ in range(10)]
        dic = collections.Counter(s)
        
        for idx in range(10): #按digit数组的顺序遍历0~9
            cnt = dic[find[idx]] #看看可以组成几个digit[idx]
            record[digit[idx]] += cnt #记录下来
            dic = dic - collections.Counter(order[idx] * cnt) #字典里减去对应的字母
                
            if not dic:
                break
            
        ress = ""
        for i in range(10): #转换成题目需要的格式
            ress += str(i) * record[i]
            
        return ress
        