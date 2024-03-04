def solution(n):
    answer = 0
    n = n - 1 if n % 2 == 1 else n
    while n > 0:
        answer += n
        n = n - 2
    return answer