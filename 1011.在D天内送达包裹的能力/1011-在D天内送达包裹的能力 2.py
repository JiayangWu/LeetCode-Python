class Solution(object):
    def shipWithinDays(self, weights, D):
        """
        :type weights: List[int]
        :type D: int
        :rtype: int
        """
        lo, hi = max(weights), sum(weights)
        while(lo <= hi):
            mid = (lo + hi) // 2 # mid ��Ϊ��ǰ���͵�capacity
            
            #------����Ϊģ���˻��Ĺ��̣�temp��ʾ��ǰ���������ص�������day��ʾ���õ�����-------
            temp = 0
            day = 1
            for weight in weights:
                temp += weight
                if temp > mid:# ��ǰ���˲���
                    day += 1
                    temp = weight
            #------����Ϊģ���˻��Ĺ���-----------------
            
            if day > D: # ��ǰ��capacity̫С�ˣ���������Ҫ�����������ܼ�ʱ����
                lo = mid + 1
            elif day <= D:
                hi = mid - 1

        return lo