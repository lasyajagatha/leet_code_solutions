class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        for i in range(0,len(matrix)):
            l=0
            r=len(matrix[i])-1
            while(l<=r):
                mid=(l+r)//2
                print(mid,i)
                if(matrix[i][mid]==target):
                    return      True
                elif (matrix[i][mid]<target):
                    l=mid+1
                else:
                    r=mid-1
        return False
        
        