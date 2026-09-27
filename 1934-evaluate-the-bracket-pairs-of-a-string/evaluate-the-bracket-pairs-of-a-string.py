class Solution(object):
    def evaluate(self, s, kn):
        """
        :type s: str
        :type knowledge: List[List[str]]
        :rtype: str
        """
        h=dict(kn)
        k=[]
        t=""
        n,m,i=-1,0,0
        a=0
        p=[]
        while(i<len(s)):
            if(s[i]=="("):
                i=i+1
                m=1
                while(s[i]!=')'):
                    k.append(s[i])
                    i=i+1
                i=i+1
                t="".join(k)
            if(m==1):
                p.append(h.get(t,"?"))
                m,a=0,0
                k=[]
            else:
                p.append(s[i])
                i=i+1
        o="".join(p)
        return o


            
        