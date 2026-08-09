class Solution(object):
    def isAnagram(self, p, q):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s=list(p)
        t=list(q)
        if(len(s)==len(t)):
            s.sort()
            t.sort()
            print(s,t)
            if(s == t):
                #print(s,t)
                return True
        return False
        