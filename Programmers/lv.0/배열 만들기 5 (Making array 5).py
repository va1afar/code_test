# link :: https://school.programmers.co.kr/learn/courses/30/lessons/181912

def solution(intStrs, k, s, l):
    answer = []
    
    for intStr in intStrs:
        if int(intStr[s:s+l]) > k:
            answer.append(int(intStr[s:s+l]))
    
    return answer