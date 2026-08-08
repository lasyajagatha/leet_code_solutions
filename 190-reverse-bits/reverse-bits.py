class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        s=format(n,'b')
        l=len(s)
        l=32-len(s)
        e=[]
        for i in range(0,l):
           e.append('0')
        f="".join(e)
        s=f+s
        s=s[::-1]
        print(s)
        t=int(s,2)
        return t