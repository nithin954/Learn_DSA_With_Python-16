def rearrange(num):
    res =[None]*len(num)
    pos=0
    neg=1
    for i in range(0,len(num)):
        if num[i]>=0:
            res[pos] = num[i]
            pos +=2
        else:
            res[neg] = num[i]
            neg+=2
    return res
        
        
num = [5,10,-3, -1, -10, 6]
print(rearrange(num))