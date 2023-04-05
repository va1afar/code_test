# link :: https://school.programmers.co.kr/learn/courses/30/lessons/120907

def solution(quiz):
    answer = []
    tmp = []
    X = 0
    Y = 0
    Z = 0
    
    for i in quiz:
        tmp = i.split(" ") #['3', '-', '4', '=', '-3']のような形になります。
        X = int(tmp[0])
        Y = int(tmp[2])
        Z = int(tmp[4])
        if tmp[1] == "+" and X+Y == Z:
            answer.append("O")
        elif tmp[1] == "-" and X-Y == Z:
            answer.append("O")
        else:
            answer.append("X")
    
    
    return answer