def solution(array, commands):
    answer = []
    for i in commands:
        left = int(i[0]) - 1
        right = int(i[1])
        num = int(i[2]) - 1

        arr = array[left:right]
        arr.sort()

        answer.append(arr[num])
    return answer