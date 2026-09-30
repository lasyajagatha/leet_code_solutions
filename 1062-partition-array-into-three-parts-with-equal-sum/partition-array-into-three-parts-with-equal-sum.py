class Solution(object):
    def canThreePartsEqualSum(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        s=sum(arr)
        if(s%3!=0):
            return False
        t=s//3
        c=0
        a=0
        for i in range(0,len(arr)):
            c=c+arr[i]
            if(c==t):
                a=a+1
                c=0
        if(a>=3):
            return True
        return False

