class Solution(object):
    def addStrings(self, nums1, nums2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if not nums1:
            return nums2
        elif not nums2:
            return nums1
        elif not nums1 and not nums2:
            return ""
        
        l1, l2 = len(nums1), len(nums2)
        if l1 > l2: #±£Ö¤ l1 ½Ï¶Ì
            l1, l2 = l2, l1
            nums1, nums2 = nums2, nums1
        n1 = list(nums1)[::-1]
        n2 = list(nums2)[::-1]
        
        res = list()
        for i in range(0, l2):
            if i < l1:
                res.append(int(n1[i]) + int(n2[i]))
            else:
                res.append(int(n2[i]))
        
        # print res
        for i in range(0, l2):
            while(res[i] > 9):
                res[i] -= 10
                if i != l2 - 1:
                    res[i + 1] += 1
                else:
                    res.append(1)
                    l2 += 1
                    
        return "".join(str(res[i]) for i in range(l2 - 1, -1, -1))
        
        