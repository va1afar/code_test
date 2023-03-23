# link :: https://school.programmers.co.kr/learn/courses/30/lessons/120904

def solution(num, k):
    answer = -1
    list_num = str(num)
    
    for i, word in enumerate(list_num):
        if int(word) == k:
            answer = i+1
            break
        
    return answer