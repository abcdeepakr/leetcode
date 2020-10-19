class Solution:
    def searchMatrix(self, matrix, target):
        row  = len(matrix)
        if(matrix == []):
            return False
        elif(row==1):
            if(target in matrix[0]):
                return True
            else:
                return False
        else:
            col = len(matrix[0])
            row_to_be_searched = row-1
            for i in range(row-1):
                if(target<matrix[i+1][0] and target>=matrix[i][0]):
                    row_to_be_searched = i
                    break
            if(target in matrix[row_to_be_searched]):
                return True
            else:
                return False
        '''
        overall = []
        for i in matrix:
            overall+=i
        if(target in overall):
            return True
        else:
            return False
        '''