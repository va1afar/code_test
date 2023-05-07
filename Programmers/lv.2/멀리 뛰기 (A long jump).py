# link :: https://school.programmers.co.kr/learn/courses/30/lessons/12914

def solution(n):
    answer = 0
    list_n = [1, 1]
    
    # フィボナッチ数列のような規則性があります。
    # ex) [1, 1, 2, 3, 5, 8, 13, ...]
    for i in range(2, n+1):
        list_n.append(list_n[i-2] + list_n[i-1])
    answer = list_n[n] % 1234567
    
    return answer