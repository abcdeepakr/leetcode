num = 6996
maximum = num
temp = ""
for i in (str(num)):
    temp+= i + " "
digits = temp.split()
for i in range(len(digits)):
    if(digits[i]=="9"):
        new = "".join(digits[:i]) +"6" + "".join(digits[i+1:])
        maximum = max(int(new),maximum)
    else:
        new = "".join(digits[:i]) +"9" + "".join(digits[i+1:])
        maximum = max(int(new),maximum)
print(maximum)
