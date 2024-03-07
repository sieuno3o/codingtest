def solution(num_list):
    a = sum(num_list)
    b = 1
    for i in num_list:
        b *= i

    if a**2 > b:
        answer = 1
    else:
        answer = 0
    return answer