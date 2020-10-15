class Solution:
  def generate(numRows):
      matrix  = [[1],[1,1]]
      if(numRows==0):
          return []
      elif(numRows == 1):
          return([[1]])
      elif(numRows==2):
          return([[1],[1,1]])
      else:
          for i in range(2,numRows):
              inner = [1]*1
              for j in range(i-1):
                  inner.append(matrix[i-1][j]+matrix[i-1][j+1])
              inner.append(1)
              matrix.append(inner)
          return matrix