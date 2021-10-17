m = int(input())
n = int(input())
l1 = []
l2 = []
flag = 0
for i in range(1,m+1):
    if m % i == 0:
        l1.append(i)
for j in range(1,n+1):
    if n % j == 0:
        l2.append(j)
for x in range(1,len(l1)):
    for y in range(1,len(l2)):
        if(l1[x] == l2[y]):
            flag = 1
if (flag == 1):
    print("Not coprime")
else:
    print("Coprime")