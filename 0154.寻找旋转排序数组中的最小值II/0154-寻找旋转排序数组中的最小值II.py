class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            
            if nums[mid] > nums[right]: #最小值肯定在【mid + 1, right】
                left = mid + 1
            elif nums[mid] < nums[right]: #最小值肯定在【left, mid】
                right = mid
            elif nums[mid] == nums[right]: #无法确定最小值的区间
                
                flag = False
                for j in range(right - 1, mid, -1):#逐个在右侧找，看是不是有比nums[mid]更小的数
                    if nums[mid] > nums[j]:
                        flag = True #确实存在更小的数，是nums[j]
                        break
                        
                if flag: #可以确定最小值肯定在【mid + 1, j】
                    left = mid + 1
                    right = j
                else: #mid 到right所有的数都相等, 最小值肯定在【left, mid】
                    right = mid
                    
        return nums[left]
                    