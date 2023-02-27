# link :: https://school.programmers.co.kr/learn/courses/30/lessons/12935

def solution(arr):
    answer = []
    tmp = 0
    
    if len(arr) == 1:
        answer.append(-1)
    else:
        tmp = arr[0]
        for i in arr:
            if tmp > i:
                tmp = i
        arr.remove(tmp)
        answer = arr
    
    return answer
