# link :: https://school.programmers.co.kr/learn/courses/30/lessons/82612

def solution(price, money, count):
    answer = 0
    
    for i in range(count):
        money -= price*(i+1) 
    if money < 0:
        answer = -(money)
        

    return answer
