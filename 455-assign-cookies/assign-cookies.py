class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort(reverse=True)
        s.sort(reverse=True)
        c=0
        j=0
        for i in g:
            if(j<len(s) and s[j]>=i):
                c=c+1
                j=j+1
        return c
        