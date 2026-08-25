class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        l=[]
        n=len(matrix)
        for i in range(0,n):
            for j in range(0,n):
                l.append(matrix[i][j])
        l.sort()
        return l[k-1]
            

        