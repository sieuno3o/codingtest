import sys
sys.setrecursionlimit(10**6)
n, m, k = map(int, input().split())

# 0이 빈곳이고 1이 쓰레기가 있는 곳으로 설정
# index를 1부터 사용하기 위해 n+1, m+1로 설정
graph = [[0] * (m + 1) for _ in range(n + 1)]

# 쓰레기가 있는 곳의 좌표를 입력 받아 그래프에 1을 삽입
for _ in range(k):
    x, y = map(int, input().split())
    graph[x][y] = 1

# 쓰레기 크기 반환 함수 정의 
def dfs(x, y):

    # graph 범위를 벗어나면 0 반환
    if x <= 0 or x > n or y <= 0 or y > m:
        return 0
    
    # 쓰레기가 해당 위치에 있다면 
    if graph[x][y] == 1:
        # 해당 위치를 방문 처리
        graph[x][y] = 0
        # 현재 위치 + 상하좌우 쓰레기 개수 모두 합하여 반환
        return 1 + dfs(x + 1, y) + dfs(x - 1, y) + dfs(x, y + 1) + dfs(x, y - 1)
    
    return 0

max_size = 0

for i in range(1, n + 1):
    for j in range(1, m + 1):
        if graph[i][j] == 1:
            # 모든 위치에서 DFS를 실행하여 가장 큰 쓰레기 더미의 크기를 찾음
            max_size = max(max_size, dfs(i, j))

print(max_size)