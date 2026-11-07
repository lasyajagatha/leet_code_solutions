class Solution:
    def smallestNumber(self, n: int) -> int:
        if(n==1):
            return 1
        x=math.log(n,2)
        i,s=0,0
        while(i<=x):
            s=s+(1<<i)
            i=i+1
        return s

        