# link :: https://school.programmers.co.kr/learn/courses/30/lessons/42576

def solution(participant, completion):
    answer = ''
    dict_participant = {name : 0 for name in participant}
    
    for i in participant:
        dict_participant[i] += 1
    for i in completion:
        dict_participant[i] -= 1
    
    for key,value in dict_participant.items():
        if value != 0:
            answer = key
  
    return answer