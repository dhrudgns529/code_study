# https://www.acmicpc.net/problem/14226
# bfs, dp
# bfs와 dp가 합쳐진 문제는 처음.
# 조건이 두개(이모티콘)(클립보드)로 dp사용 중요!!
from collections import deque
s = int(input())
dp = [[-1]*1001 for _ in range(1001)]  # dp[갯수][복사된갯수]  의미 
qu = deque()
qu.append([1,0]) 
dp[1][0] = 0 # 이모티콘 1개이고 클립보드 0개 
result = 987654321 # 임의최대값
while qu: # bfs
    a, c= qu.popleft()
    if a == s: # 목표 갯수 도달
        for i in dp[a]: # 도달한 dp중에 제일 작은 값 출력
            if i != -1:
                result = min(i,result)
        print(result)
        break
    if 0 < a <= 1000 and dp[a][a] == -1: 
        dp[a][a] = dp[a][c] + 1 # 걸린 시간
        qu.append([a,a]) # 이모티콘 클립보드 복사
    if c != 0 and a+c <=1000 and dp[a+c][c] == -1:
        dp[a+c][c] = dp[a][c] +1 # 걸린 시간
        qu.append([a+c,c]) # 이모티콘 + 클립보드 (붙혀넣기)
    if a - 1 > 0 and dp[a-1][c] == -1:
        dp[a-1][c] = dp[a][c] +1 # 걸린 시간
        qu.append([a-1,c]) # 이모티콘-1
