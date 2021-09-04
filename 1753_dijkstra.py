# https://www.acmicpc.net/problem/1753
# 다익스트라 알고리즘(heapq)
import heapq, sys
input = sys.stdin.readline
v, e = map(int,input().split()) # 정점, 간선
start = int(input()) # 시작 정점의 번호
graph = [[] for _ in range(v+1)] # 그래프 넣을 리스트
for _ in range(e):
    a, b, p = map(int,input().split()) # a -> b 로 가는 값 p
    graph[a].append((b,p)) # 
distance = [1e9] * (v+1) # 기본 값 무한대(INF)
def dijkstra(start): # 다익스트라
    q = [] 
    heapq.heappush(q,(0, start)) # q에 값 0, 시작점 start
    distance[start] = 0 # 시작점 값 0
    while q:
        dist, now = heapq.heappop(q) 
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1] # cost = dist(현지점까지의 최소값) + i[1](현재점에서 i[0]까지의 값)
            if cost < distance[i[0]]: # cost가 더 작은 값일때
                distance[i[0]] = cost # 초기화
                heapq.heappush(q,(cost,i[0])) 
dijkstra(start)
for i in range(1,v+1):
    if distance[i] == 1000000000:
        print("INF")
    else:
        print(distance[i])
        