class Solution(object):
    def rowAndMaximumOnes(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        j=0
        m=0
        for i in mat:
            if(sum(i)>m):
                m=sum(i)
                j=mat.index(i)
        k=[]
        k.append(j)
        k.append(m)
        return k
        
        