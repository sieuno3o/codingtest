def solution(num_list, n):
    answer1 = num_list[n:]
    answer2 = num_list[:n]
    print(answer1, answer2)
    return answer1 + answer2