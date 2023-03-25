# link :: https://school.programmers.co.kr/learn/courses/30/lessons/12921

# blogged link ::https://medium.com/@va1afar.biz/programmers-coding-test-lv-1-finding-prime-numbers-f2d45ad69161

import math

def solution(n):
    answer = 0
    # [0]から[n]までTrueが入ったリストを作成
    array = [True for i in range(n+1)] 
    sqrt_n = int(math.sqrt(n))
    
    # 「エラトステネスの篩」アルゴリズムで素数じゃない数字を消していきます。
    for i in range(2, sqrt_n+1):
        if array[i] == True:
            multiple = i
            for j in range(i*2, n+1, i):
                array[j] = False
    for k in range(2, n+1):
        if array[k] == True:
            answer += 1
        
    return answer