class Solution(object):
    def dayOfYear(self, date):
        """
        :type date: str
        :rtype: int
        """
        p=map(int,date.split("-"))
        print(p)
        s=0
        l=[31,28,31,30,31,30,31,31,30,31,30,31]
        if(p[1]==1):
            return p[2]
        else:
            for i in range(0,p[1]-1):
                s=s+l[i]
            s=s+p[2]
        if(p[1]!=2):
            if(  p[0]%100==0 ):
                if(p[0]%400==0):
                    return s+1
            elif(p[0]%4==0):
                return s+1
        return s
        
        