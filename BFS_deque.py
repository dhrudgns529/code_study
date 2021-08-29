from collections import deque # deque 사용 

# BFS 메서드 정의
def bfs(graph, start, visited):
    queue = deque([start]) # deque 구현

    visited[start] = True # 현재 노드 방문 처리

    while queue: # 빌 때까지 반복
        v = queue.popleft() # 첫 원소 뽑아 저장
        print(v, end=' ')

        for i in graph[v]: 
            if not visited[i]:
                queue.append(i)
                visited[i] = True
# 각 노드 연결 정보 (2차원 리스트)
graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7],
]
# 각 노드 방문 정보 (1차원 리스트)
visited = [False] * 9

bfs(graph, 1, visited)