# This program is for finding fibbonaci series


val=int(input())
f0,f1=0,1
for i in range(0,val+1):
    if i==0:
        print(0)
    else:
        f0,f1=f1,f0+f1
        print(f0)
    
