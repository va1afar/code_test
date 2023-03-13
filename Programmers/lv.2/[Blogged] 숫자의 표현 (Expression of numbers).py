# link :: https://school.programmers.co.kr/learn/courses/30/lessons/12924

# blogged link :: https://medium.com/@va1afar.biz/programmers-coding-test-lv-2-expression-of-numbers-b099784817d4

def solution(n):
    answer = 0
    list_n = []
    
    for i in range(1, n+1):
        for j in range(i, n+1):
            list_n.append(j)
            if sum(list_n) == n:
                list_n = []
                answer += 1
                break
            elif sum(list_n) > n:
                list_n = []
                break
        
    return answer
