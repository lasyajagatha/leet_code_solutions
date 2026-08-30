class Solution(object):
    def checkDivisibility(self, n):
        """
        :type n: int
        :rtype: bool
        """
        p,k=n,1
        s=0
        while(p>0):
            s=s+(p%10)
            k=k*(p%10)
            p=p//10
        s=s+k
        if(n%s==0):
            return True
        else:
            return False
    


        