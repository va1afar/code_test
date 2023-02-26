# link :: https://school.programmers.co.kr/learn/courses/30/lessons/12919

def solution(seoul):
    answer = ''
    
    for num,name in enumerate(seoul):
        if name == "Kim":
            answer = "김서방은 "+str(num)+"에 있다"
    
    return answer
