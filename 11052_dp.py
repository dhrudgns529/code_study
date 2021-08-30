#https://www.acmicpc.net/problem/11052
N = int(input())
p = [0] + list(map(int,input().split())) # 1 5 6 7
dp = [0 for _ in range(N+1)] # dp[i] < i개 뽑았을때 최댓값 저장

for i in range(1,N+1):
    for k in range(1,i+1):
        dp[i] = max(dp[i], dp[i-k] + p[k])
print(dp[i])

# n = 4
# 1 5 6 7
