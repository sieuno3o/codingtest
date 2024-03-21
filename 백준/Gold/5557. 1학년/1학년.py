n = int(input())

dp = [[0 for _ in range(21)] for _ in range(n)]
# dp[i][j] -> i번째 숫자까지 고려했을 때, 합이 j가 되는 경우의 수

arr = list(map(int, input().split()))

# 첫번째 수 저장
dp[0][arr[0]] = 1

# 마지막 숫자를 제외하고 순회
for i in range(1, n-1):
    for j in range(21): # 모든 경우의 수에 대해 
        if dp[i - 1][j]: # 이전 단계에서 j값을 만들 수 있는 경우의 수가 있다면 
            # 숫자를 더했을떄 범위 내에 있다면 
            if 0 <= j + arr[i] <= 20:
                dp[i][j + arr[i]] += dp[i - 1][j]
            # 숫자를 뺐을때 범위 내에 있다면 
            if 0 <= j - arr[i] <= 20:
                dp[i][j - arr[i]] += dp[i - 1][j]

# 입력받았던 숫자 중 마지막 숫자와 일치하는 경우의 수가 얼마인지 출력
print(dp[n-2][arr[-1]])