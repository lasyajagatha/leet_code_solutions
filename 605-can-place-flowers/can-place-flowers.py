class Solution(object):
    def canPlaceFlowers(self, f, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        if(len(f)>1):
            if(f[0]==0 and f[1]==0):
                f[0]=1
                n=n-1
            for i in range(1,len(f)-1):
                if(f[i-1]==0 and f[i]==0 and f[i+1]==0 ):
                    f[i]=1
                    n=n-1
            if(f[len(f)-2]==0 and f[len(f)-1]==0):
                n=n-1
                f[i]=1
            print(n)
            if(n>0):
                return False
            else:
                return True
        else:
            if((f[0]==0 and n==1) or n==0):
                return True
            else:
                return False

        
        