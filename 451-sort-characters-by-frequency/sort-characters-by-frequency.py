class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        l=[]
        p=[]
        for i in s:
            if(i not in p):
                p.append(i)
                l.append(s.count(i))
        print(p,l)
        r=[]
        n=len(p)
        while True:
            if(l==[]):
                break
            g=max(l)
            print(g)
            j=l.index(g)
            print(j)
            for i in range(g):
                r.append(p[j])
            l.remove(g)
           
            p.remove(p[j])

        return "".join(r)


       
        