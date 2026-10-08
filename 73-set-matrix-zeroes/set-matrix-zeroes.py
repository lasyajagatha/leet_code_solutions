class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])

        r = set()
        c = set()

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    r.add(i)
                    c.add(j)

        for i in r:
            for j in range(cols):
                matrix[i][j] = 0

        for j in c:
            for i in range(rows):
                matrix[i][j] = 0
        