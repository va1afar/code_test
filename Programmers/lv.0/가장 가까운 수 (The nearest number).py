# link :: https://school.programmers.co.kr/learn/courses/30/lessons/120890

def solution(array, n):
    answer = 0
    storage = 0
    
    storage = array[0]
    for i in array:
        if abs(n - i) < abs(n - storage):
            storage = i
        elif abs(n - i) == abs(n - storage):
            storage = min(i, storage)
    answer = storage
    
    return answer