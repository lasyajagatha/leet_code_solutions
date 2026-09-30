class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        k,t,tw=0,0,0
        for i in bills:
            if(i==5):
                k=k+1
            elif(i==10):
                t=t+1
                if(k<=0):
                    return False
                k=k-1
            else:
                if(k<=0):
                    return False
                if(t>0):
                    t=t-1
                    k=k-1
                else:
                    if(k<3):
                        return False
                    else:
                        k=k-3
        return True
        