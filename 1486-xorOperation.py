#32 ms	14.2 MB

def xorOperation0(n = 5, start = 0):
    ans = 0
    for i in range(n):
        curr = start + 2*i
        ans  = ans ^ curr
    return ans

#####################################

# 28 ms	14 MB

def xorOperation1(n = 5, start = 0):
    ans = 0
    for i in range(n):
        ans  ^= start + (2*i)
    return ans