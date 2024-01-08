def solution(s):
    answer = 0
    temp = s.split(" ")

    for i in range(len(temp)):  # temp 리스트 길이만큼 반복
        if temp[i] == "Z":  # 만약 temp[i]가 Z라면
            answer -= int(temp[i - 1])  # Z 전 숫자를 빼줌
        else:
            answer += int(temp[i])
        
    return answer