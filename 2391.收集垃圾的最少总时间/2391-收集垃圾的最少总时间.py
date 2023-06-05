class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        t_m, t_p, t_g = 0, 0, 0
        
        driving_time_m = 0
        driving_time_p = 0
        driving_time_g = 0
        for index, g in enumerate(garbage):
            # M
            count_m = g.count("M")
            if index:
                driving_time_m += travel[index - 1]
            if count_m:
                t_m += count_m
                t_m += driving_time_m
                driving_time_m = 0
            

            count_p = g.count("P")  
            if index:
                driving_time_p += travel[index - 1]
            if count_p:
                t_p += count_p
                t_p += driving_time_p
                driving_time_p = 0
                

            count_g = g.count("G")  
            if index:
                driving_time_g += travel[index - 1]
            if count_g:
                t_g += count_g
                t_g += driving_time_g
                driving_time_g = 0
               
        return t_m + t_p + t_g