class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        c=0
        s=1
        while(n>0):
            n=n-s
            s=s+1
            c=c+1
        if(n==0):
            return c
        return c-1
        
        
        