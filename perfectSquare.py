num = 4
start = 0
end = 0
if(num==1):
    print(True)
else:
    ans = num/2
    while(1):
        ans = ans//2
        if(ans**2 < num):
            start = int(ans)
            end = int(ans*2)
            break
for i in range(start, end+1):
  if(i**2 == num):
    print(True)