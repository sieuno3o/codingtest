import re


def solution(my_string):
    # 정규표현식 re.findall 함수를 사용 숫자 추출
    numbers = re.findall(r"\d+", my_string)

    if not numbers:  # 만약 리스트가 비어있다면
        answer = 0
    else:
        # 리스트 문자열 정수 변환 후 더해줌
        answer = sum(map(int, numbers))

    return answer