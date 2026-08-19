class Solution(object):
    def validDigit(self, n, x):
        """
        :type n: int
        :type x: int
        :rtype: bool
        """
        l=str(n)
        x=str(x)
        if( x in l and l[0]!=x):
            return True
        return False

        