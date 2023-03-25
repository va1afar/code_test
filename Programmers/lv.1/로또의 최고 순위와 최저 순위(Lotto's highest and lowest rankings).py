# link :: https://school.programmers.co.kr/learn/courses/30/lessons/77484#fn1

def solution(lottos, win_nums):
    answer = []
    hit_numbers = 0
    cnt_0 = 0
    
    for i in lottos:
        if i == 0:
            hit_numbers += 1
            cnt_0 += 1
        elif i in win_nums:
            hit_numbers += 1
        else:
            continue
    if hit_numbers >= 2:
        answer.append(7 - hit_numbers)
        if answer[-1] + cnt_0 <= 5:
            answer.append(answer[-1] + cnt_0)
        else:
            answer.append(6)
    else:
        answer = [6,6]
        
    return answer