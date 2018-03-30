a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
countA=0
countB=0
for i in range(0,len(a)):
    for j in range(1,len(a)-1):
        if a[j]==a[i]:
            countA=countA+1
            
for i in range(0,len(b)):
    for j in range(1,len(b)-1):
        if b[j]==b[i]:
           countB=countB+1

if countA > countB:
    print('CountA =%d ',countA)
else:
    print('CountB=%d ',countB)


