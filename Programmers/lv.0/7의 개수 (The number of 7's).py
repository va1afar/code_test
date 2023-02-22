# link :: https://school.programmers.co.kr/learn/courses/30/lessons/120912

def solution(array):
    answer = 0
    string = ""
    
    for i in array:
        string += str(i)
    for n in range(len(string)):
        if string[n] == '7':
            answer += 1
    
    return answer
