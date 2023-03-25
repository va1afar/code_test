# link :: https://school.programmers.co.kr/learn/courses/30/lessons/17682

def solution(dartResult):
    answer = 0
    score = []
    digit = ''
    
    for i, word in enumerate(dartResult):
        if word.isdigit():
            digit += word
        elif word.isalpha():
            if word == 'S':
                score.append(int(digit))
                digit = ''
            elif word == 'D':
                score.append(int(digit)**2)
                digit = ''
            elif word == 'T':
                score.append(int(digit)**3)
                digit = ''
        elif word == '*':
            score[-1] = score[-1] * 2
            if len(score) >= 2:
                score[-2] = score[-2] * 2
        elif word == '#':
            score[-1] = score[-1] * -1
    answer = sum(score)
        
    return answer