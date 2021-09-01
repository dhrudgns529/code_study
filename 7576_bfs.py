# https://www.acmicpc.net/problem/7576
# bfs
from collections import deque # deque 
m, n = map(int, input().split())
box = []

for i in range(n):
    box.append(list(map(int, input().split())))

queue = deque()
dx = [1, -1, 0, 0] # 상하좌우
dy = [0, 0, -1, 1]
def bfs(): # BFS 
    while queue:
        a, b = queue.popleft()
        for i in range(4):
            x = a + dx[i]
            y = b + dy[i]
            if 0 <= x < n and 0 <= y < m and s[x][y] == 0: # 범위 안이고, 안 익은 토마토(0)일 때
                box[x][y] = box[a][b] + 1 # 일수 확인
                queue.append([x, y])
for i in range(n):
    for j in range(m):
        if box[i][j] == 1: # 익은 토마트(1)인 경우
            queue.append([i, j])
bfs() 
isTrue = False
result = -2
for i in box:
    for j in i:
        if j == 0: # BFS를 완료 후 안 익은 토마토(0)인 경우
            isTrue = True
        result = max(result, j) # 제일 높은 수가 최대 일수
if isTrue == True: # 불가능
    print(-1)
elif result == -1:
    print(0)
else:
    print(result-1) # 1부터 시작하여 -1

# https://pacific-ocean.tistory.com/267 # 참고