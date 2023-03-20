# link :: https://school.programmers.co.kr/learn/courses/30/lessons/42840

def solution(answers):
    answer = []
    num1 = [1,2,3,4,5]
    num2 = [2,1,2,3,2,4,2,5]
    num3 = [3,3,1,1,2,2,4,4,5,5]
    cnt = [0,0,0]
    
    while len(num1) < len(answers):
        num1.extend(num1)
    while len(num2) < len(answers):
        num2.extend(num2)
    while len(num3) < len(answers):
        num3.extend(num3)
    for i in range(len(answers)):
        if answers[i] == num1[i]:
            cnt[0] += 1
        if answers[i] == num2[i]:
            cnt[1] += 1
        if answers[i] == num3[i]:
            cnt[2] += 1
    max_cnt = max(cnt)
    if cnt[0] == max_cnt:
        answer.append(1)
    if cnt[1] == max_cnt:
        answer.append(2)
    if cnt[2] == max_cnt:
        answer.append(3)
    
    return answer