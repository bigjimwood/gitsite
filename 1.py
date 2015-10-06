#coding:utf-8
#深度优先遍历
a=[[1 for i in range(0,5)] for j in range(0,5)]
i=0
j=0
while i<5 and j<5:
    if i==j:
        a[i][j]=0
        i+=1
        j+=1
    else:
        continue
a[0][3]=a[1][2]=999
a[1][4]=a[2][1]=a[2][3]=a[3][0]=a[3][2]=a[3][4]=a[4][1]=a[4][3]=999
print a



node=[0]*5
n=0
def sd(num):
    global n
    if n>4:
        return
    node[num]=1
    for i in range(0,5):
        if a[num][i]==1 and node[i]==0:
            n+=1
            print i
            sd(i)
            


sd(4)
            


