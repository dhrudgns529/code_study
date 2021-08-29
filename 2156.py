# https://www.acmicpc.net/problem/2156
# https://pacific-ocean.tistory.com/152  < 설명 참고
import sys
input = sys.stdin.readline
n = int(input()) # 1 <= n <=10000
array = [0]
dp = [0]
for _ in range(n):
    array.append(int(input()))
if n <=2: # 포도주 2개이하 일때
    print(sum(array))
else:
    dp.append(array[1]) # 포도주 1개
    dp.append(max(array[2],array[1]+array[2])) # 포도주 2개
    dp.append(max(array[2]+array[3],array[1]+array[3],array[1]+array[2])) # 포도주 3개
    for i in range(4,n+1): # dp[i] = 포도주 i개일때 최대로 마시는 양
        dp.append(max(dp[i-3]+array[i-1]+array[i],dp[i-2]+array[i],dp[i-1]))    
    print(dp[n]) 