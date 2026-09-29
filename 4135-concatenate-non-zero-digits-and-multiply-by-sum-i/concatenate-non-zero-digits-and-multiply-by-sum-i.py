class Solution(object):
    def sumAndMultiply(self, n):
        """
        :type n: int
        :rtype: int
        """
        p=str(n)
        s,t=0,0
        for i in range(0,len(p)):
            if(p[i]!='0'):
                s=s*10+int(p[i])
                t=t+int(p[i])
        print(s,t)
        return s*t
        
        