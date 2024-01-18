def solution(answers):
    
    P1 = [1, 2, 3, 4, 5]
    P2 = [2, 1, 2, 3, 2, 4, 2, 5]
    P3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    score = [0, 0, 0]
    
    for i in range(len(answers)):
        Q1 = i % 5
        Q2 = i % 8
        Q3 = i % 10

        if answers[i] == P1[Q1]:
            score[0] += 1
        if answers[i] == P2[Q2]:
            score[1] += 1
        if answers[i] == P3[Q3]:
            score[2] += 1
            
    answer = []
    for i in range(len(score)):
        if score[i] == max(score): 
            answer.append(i+1)
    
    return answer