# https://www.acmicpc.net/problem/14501
# dp (역순으로 최댓값 찾기)
n = int(input()) # 일수
T, P = [], [] # T 소요기간, P 금액
for _ in range(n):
    a, b = map(int,input().split())
    T.append(a)
    P.append(b)
dp = [0]*(n+1) 
for i in range(n-1,-1,-1):
    if T[i]+i > n: # 일수가 초과시 
        dp[n-i] = dp[n-i-1] 
    elif T[i] == 1: # T[i]가 1일때
        dp[n-i] = dp[n-i-1] + P[i]
    else: # 최댓값
        dp[n-i] = max(dp[n-i-1],dp[n-i-T[i]]+P[i])
print(max(dp))