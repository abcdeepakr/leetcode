'''
Input: ops = ["5","-2","4","C","D","9","+","+"]
Output: 27
Explanation:
"5" - Add 5 to the record, record is now [5].
"-2" - Add -2 to the record, record is now [5, -2].
"4" - Add 4 to the record, record is now [5, -2, 4].
"C" - Invalidate and remove the previous score, record is now [5, -2].
"D" - Add 2 * -2 = -4 to the record, record is now [5, -2, -4].
"9" - Add 9 to the record, record is now [5, -2, -4, 9].
"+" - Add -4 + 9 = 5 to the record, record is now [5, -2, -4, 9, 5].
"+" - Add 9 + 5 = 14 to the record, record is now [5, -2, -4, 9, 5, 14].
The total sum is 5 + -2 + -4 + 9 + 5 + 14 = 27.
'''

ops = ["5","-2","4","C","D","9","+","+"]
result = []
for i in ops:
  if(i.isnumeric()):
    result.append(int(i))
  if(len(i)==2):
    result.append(int(i))
  if(i == "C"):
    result.pop()
  if(i == "D"):
    result.append(result[len(result)-1]*2)
  if(i == "+"):
    result.append(result[len(result)-1] + result[len(result)-2])
print(sum(result))
