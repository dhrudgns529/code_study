#https://www.acmicpc.net/problem/1261
# bfs + heapq
# deque랑 heapq 차이점? 
import heapq
m, n = map(int, input().split())
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
arr = []
visit = [[0] * m for i in range(n)]
for i in range(n):
    arr.append(list(map(int, input())))
def bfs():
    heap = []
    heapq.heappush(heap, [0, 0, 0])
    visit[0][0] = 1
    while heap:
        c, a, b = heapq.heappop(heap) # c 값, a, b 위치
        if a == n - 1 and b == m - 1: # 목표 위치 도달
            print(c) # 그 때 값
            return
        for i in range(4):
            x = a + dx[i]
            y = b + dy[i]
            if 0 <= x < n and 0 <= y < m and visit[x][y] == 0: # 범위 안, 방문하지 않은 곳
                if arr[x][y] == 1: # 벽일 경우
                    heapq.heappush(heap, [c + 1 , x, y])
                else: # 벽 아닐 경우
                    heapq.heappush(heap, [c, x, y])
                visit[x][y] = 1 # 방문 처리
bfs()