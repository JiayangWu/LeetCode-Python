class Solution(object):
    def isRobotBounded(self, ins):
        """
        :type instructions: str
        :rtype: bool
        """
        ins = ins * 4
        state = "N"
        xx, yy = 0, 0
        for i, x in enumerate(ins):
            if state == "N":
                if x == "G":
                    yy += 1
                elif x == "L":
                    state = "W"
                elif x == "R":
                    state = "E"
                    
            elif state == "W":
                if x == "G":
                    xx -= 1
                elif x == "L":
                    state = "S"
                elif x == "R":
                    state = "N"
                    
            elif state == "S":
                if x == "G":
                    yy -= 1
                elif x == "L":
                    state = "E"
                elif x == "R":
                    state = "W"
                    
            elif state == "E":
                if x == "G":
                    xx += 1
                elif x == "L":
                    state = "N"
                elif x == "R":
                    state = "S"
            print xx, yy, state
                    
        # print xx, yy
        return xx == 0 and yy == 0
                
                    
                    
                    
                    
                
        