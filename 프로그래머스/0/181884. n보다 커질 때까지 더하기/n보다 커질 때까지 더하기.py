def solution(numbers, n):
    answer = 0
    for i in numbers:
        if answer + i > n:
            return answer + i
        answer += i