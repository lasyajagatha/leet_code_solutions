class Solution(object):
    def sumZero(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        l=[]
        if(n%2==0):
            c,p=0,-1
            while(c<n/2):
                l.append(p)
                p=p-1
                c=c+1
            c,p=0,1
            while(c<n/2):
                l.append(p)
                p=p+1
                c=c+1
            return l
        else:
            c,p=0,-1
            while(c<n/2):
                l.append(p)
                p=p-1
                c=c+1
            c,p=0,1
            while(c<n/2):
                l.append(p)
                p=p+1
                c=c+1
            l.append(0)
            return l
       
        