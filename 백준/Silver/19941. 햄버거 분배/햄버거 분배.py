N, K = map(int, input().split())
location = list(input())
count = 0

for i in range(N):
    if location[i] == 'P': # 현재 위치가 사람이라면 
        for j in range(max(i-K, 0), min(i+K+1, N)): # 범위 제한  
            # 해당 범위 내에서 햄버거를 찾았을 경우
            if location[j] == 'H':
                location[j] = 0 # 방문처리 
                count += 1 # 카운팅 
                break

print(count)
