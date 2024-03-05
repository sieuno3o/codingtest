def solution(message):
    a = message.replace(" ",".")
    answer = len(list(a)) * 2
    return answer