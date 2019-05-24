class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        left, right = 0, 0
        queue = []
        last_pos = {}
        res = 0
        for right in range(len(s)):
            if s[right] in queue:
                last_pos[s[right]] = right
            elif s[right] not in queue:
                if len(queue) >= 2:

                    if last_pos[queue[0]] < last_pos[queue[1]]: #°Ñ0ºÅÔªËØÌßµô
                        left = last_pos[queue[0]] + 1
                        last_pos.pop(queue[0])
                        queue.pop(0)
                    else:
                        left = last_pos[queue[1]] + 1
                        last_pos.pop(queue[1])
                        queue.pop(1)
                        
                queue.append(s[right])
                last_pos[s[right]] = right
            # print s[left:right + 1]
            res = max(res, right - left + 1)
        return res
                        
        return res 