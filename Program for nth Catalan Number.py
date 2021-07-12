# Dynamic Programming
n=int(input())                      # input your catalan here
if n==0:
    print(0)
    exit(1)
dp=[0]*n
dp[0]=1
if n>=2:
    dp[1]=1
for i in range(2,len(dp)):
    sumis=0
    ctr=i-1
    for j in range(i):
        
        sumis=sumis+dp[ctr]*dp[j]
        ctr-=1
    dp[i]=sumis
print(dp[n-1])
