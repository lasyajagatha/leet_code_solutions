class Solution(object):
    def largestOddNumber(self, num):
        """
        :type num: str
        :rtype: str
        """
        l=list(map(int,num))
        j=0
        for i in range(len(l)-1,-1,-1):
            if(l[i]%2!=0):
                j=1
                print(l[i])
                break
        if(j==0):
            return ""
        
        return num[0:i+1]
        