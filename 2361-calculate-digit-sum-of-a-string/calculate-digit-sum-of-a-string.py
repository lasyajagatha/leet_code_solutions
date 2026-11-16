class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while(len(s)>k):
            l=[]
            su,i=0,0
            while(i<len(s)):
                if((i+1)%k==0):
                    su=su+(ord(s[i])-ord('0'))
                    l.append(su)
                    su=0
                    x=i
                else:
                    su=su+(ord(s[i])-ord('0'))
                    #print(su,i)
                i=i+1
            if(x!=len(s)-1):
                l.append(su)
            p=map(str,l)
            s="".join(p)
            print(s)
        return s


            


        