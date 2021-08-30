# https://www.acmicpc.net/problem/13023
# dfs 이용 
# a, b 를 받아 arr에 넣을때 서로서로 넣어야하는 부분 생각
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
arr = [[] for i in range(n)]
visited = [False] * n # 모든 노드 방문X

for _ in range(m):
    a, b = map(int,input().split())
    arr[a].append(b) # a가 b랑 친구인것은
    arr[b].append(a) # b가 a랑 친구인것과 같다 # 둘은 친구사이


def dfs(depth, v):
    if depth == 4: # A, B, C, D, E 모두 만족 = 깊이가 4
        print(1)
        exit()
    for i in arr[v]:
        if not visited[i]: # 방문하지 않았을때 실행
            visited[i] = True # 방문처리
            dfs(depth+1, i)
            visited[i] = False

# 처음부터 마지막 노드까지 해당 깊이까지 들어가는 것이 있는지 탐색
for i in range(n):
    visited[i] = True 
    dfs(0, i)
    visited[i] = False

print(0)