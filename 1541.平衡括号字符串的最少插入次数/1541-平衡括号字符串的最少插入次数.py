class Solution(object):
    def minInsertions(self, s):
        """
        :type s: str
        :rtype: int
        """
        left_cnt, cons_right_cnt = 0, 0
        res = 0
        for ch in s:
            if ch == "(":
                if cons_right_cnt:
                    if cons_right_cnt % 2: # add 1 to make it even
                        res += 1
                        cons_right_cnt += 1
                    pair = min(left_cnt, cons_right_cnt // 2) # build all possible pairs
                    left_cnt -= pair
                    cons_right_cnt -= pair * 2

                    if cons_right_cnt: # if two or more ) left
                        res += cons_right_cnt // 2 # add "(" every 2 )
                        cons_right_cnt = 0
                left_cnt += 1
            else:
                cons_right_cnt += 1

        if cons_right_cnt:
            if cons_right_cnt % 2: # add 1 to make it even
                res += 1
                cons_right_cnt += 1
            pair = min(left_cnt, cons_right_cnt // 2) # build all possible pairs
            left_cnt -= pair
            cons_right_cnt -= pair * 2

            if cons_right_cnt: # if two or more ) left
                res += cons_right_cnt // 2 # add "(" every 2 )
                cons_right_cnt = 0

        res += left_cnt * 2 # add 2 ) every (
        return res