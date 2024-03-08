def solution(n):
    if n % 2 == 0:
        answer = 0
        for i in range(int(n/2)):
            answer += n**2
            n -= 2
    else:
        answer = 1
        for i in range(int(n/2)):
            answer += n
            n -= 2
    return answer