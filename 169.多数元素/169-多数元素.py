class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        vote = None
        vote_cnt = 0
        
        for num in nums:
            if not vote or num == vote:
                vote = num
                vote_cnt += 1
            else:
                vote_cnt -= 1
                if vote_cnt == 0:
                    vote = num
                    vote_cnt = 1
        return vote