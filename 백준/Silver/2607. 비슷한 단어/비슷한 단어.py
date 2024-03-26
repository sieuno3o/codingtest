N = int(input())
target = list(input()) # 기준 단어 저장
answer = 0

for _ in range(N - 1):
    compare = target[:] # 복사해서 compare에 저장 
    word = input() # 새로운 단어 저장 
    count = 0

    for w in word:
        if w in compare: # 기준 단어 안에 현재 문자가 있다면
            compare.remove(w) # 중복 카운트 방지를 위해 해당 문자 제거 
        else: 
            count += 1

    # count가 1 미만이고 compare의 길이도 1 미만이어야 함
    if count < 2 and len(compare) < 2:
        answer += 1

print(answer)