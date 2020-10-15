class Solution:
    def setZeroes(matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        vertices = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if(matrix[i][j]==0):
                    vertices.append([i,j])
        for i in vertices:
            for j in range(len(matrix[0])):
                matrix[i[0]][j]=0
        for i in vertices:
            for j in range(len(matrix)):
                matrix[j][i[1]]=0
        return matrix
        