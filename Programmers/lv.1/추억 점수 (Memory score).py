# link :: https://school.programmers.co.kr/learn/courses/30/lessons/176963

def solution(name, yearning, photo):
    answer = []
    score = 0
    
    for i in photo:
        for j in i:
            for k, word in enumerate(name):
                if j == word:
                    score += yearning[k]
        answer.append(score)
        score = 0
    
    return answer