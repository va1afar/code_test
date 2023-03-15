# link :: https://school.programmers.co.kr/learn/courses/30/lessons/12906

def solution(arr):
    answer = []
    
    answer.append(arr[0]) # i=0の時、IndexErrorが発生すため追加
    for i in arr:
        if answer[-1] != i:
            answer.append(i)
    
    return answer