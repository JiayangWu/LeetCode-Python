class Solution(object):
    def reverseWords(self, string):
        """
        :type str: List[str]
        :rtype: None Do not return anything, modify str in-place instead.
        """
        l = len(string)
        if not l:
            return 
        
        def reverse(start, end): #工具函数，功能是将string[start:end + 1]翻转
            left, right = start, end
            while(left < right):
                string[left], string[right] = string[right], string[left]
                left += 1
                right -= 1
        
        reverse(0, l - 1) #先整个翻转
        first_char_idx = 0
        for i, x in enumerate(string):
            if x == " ":
                reverse(first_char_idx, i - 1) #再把每个单词进行翻转
                first_char_idx = i + 1

        reverse(first_char_idx, l - 1)#把最后一个单词翻转