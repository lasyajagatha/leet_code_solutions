class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        m=[]
        l,r=0,0
        c=0
        while(r<len(chars)):
            if(chars[l]==chars[r]):
                  r=r+1
                  c+=1
                  if((r+1)>len(chars)):
                    m.append(chars[l])
                    if(c>1):
                        v=str(c)
                        z=list(v)
                        m=m+z
                    l=r
                    print(l,r)
                    c=0
            else:
                m.append(chars[l])
                if(c>1):
                    v=str(c)
                    z=list(v)
                    m=m+z
                l=r
                print(l,r)
                c=0
        if(len(chars)!=1):
            for i in range(0,len(m)):
                chars[i]=m[i]
        return len(m)
