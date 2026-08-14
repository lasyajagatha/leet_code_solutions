class Solution(object):
    def canBeEqual(self, m1, m2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        s1=list(m1)
        s2=list(m2)
        if(s1 == s2):
            return True
        s1[0],s1[2]=s1[2],s1[0]
        print(s1)
        if(s1 == s2):
            return True
        s1[3],s1[1]=s1[1],s1[3]
        print(s1,s2)
        if(s1 == s2):
            return True
        s1[0],s1[2]=s1[2],s1[0]
        if(s1 == s2):
            return True
        return False