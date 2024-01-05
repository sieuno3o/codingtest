def solution(my_string):
    answer = []
    
    for x in my_string:
        if x.isdigit():  # 문자가 숫자인 경우에만 
            answer.append(int(x))  # 문자를 정수로 반환하여 리스트에 추가
            
    answer.sort()  # 리스트 오름차순 정렬
    return answer
