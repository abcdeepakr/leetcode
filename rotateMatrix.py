#transpose
'''
matrix = [[1,2,3],[4,5,6],[7,8,9]]
row = len(matrix)
col = len(matrix[0])
for i in range(row):
  for j in range(i,col):
    temp = matrix[i][j]
    matrix[i][j] = matrix[j][i]
    matrix[j][i] = temp
print(matrix)
'''
matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
row = len(matrix)
col = len(matrix[0])
for i in range(row):
  for j in range(i,col):
    temp = matrix[i][j]
    matrix[i][j] = matrix[j][i]
    matrix[j][i] = temp
print(matrix)
for i in range(len(matrix)):
  x = matrix[i][::-1]
  matrix[i] = x
print(matrix)
