array = [int(input()) for _ in range(9)]
excess_height = sum(array) - 100

for i in range(9):
    for j in range(i + 1, 9):
        if array[i] + array[j] == excess_height:
            del array[j], array[i]
            array.sort()  # 남은 일곱 난쟁이의 키를 정렬
            for height in array:
                print(height)  # 정렬된 키 출력
            exit()  # 프로그램 종료
