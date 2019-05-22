class Solution(object):
    def hasGroupsSizeX( self,deck):
        """
        :type deck: List[int]
        :rtype: bool
        """
        if len(deck) <=0:
            return False
        deck.sort()
        print deck
        a = deck[0]
        count = deck.count(a)
        if count < 2:
            return False
        for j in range(2, count +1):
            if len(deck) % j != 0:
                continue
                print "invalid length",j,len(deck)
            for i in range(0, len(deck),j):
                temp = deck[i]
                flag = 0
                print i,temp
                for k in range(i,i+j):
                    if deck[k] != temp:
                        flag = 1
                        print "not the same",deck[k],temp
                if flag == 1:
                    break
            if flag == 1:
                continue
            return True
        return False


        
        