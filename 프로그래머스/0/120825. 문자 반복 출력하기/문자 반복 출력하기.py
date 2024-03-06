def solution(my_string, n):
    answer = ''
    for w in my_string:
        answer+= w*n 
    return answer