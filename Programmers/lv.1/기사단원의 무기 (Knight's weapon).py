# link :: https://school.programmers.co.kr/learn/courses/30/lessons/136798

import math

def solution(number, limit, power):
    answer = 0
    cnt = 0
    
    #　時間計算量のために、「sqrt(i)」まで確認します。
    for i in range(1, number+1):
        sqrt_i = int(math.sqrt(i))
        for j in range(1, sqrt_i+1):
            if i % j == 0:
                cnt += 2
        if sqrt_i**2 == i:
            cnt -= 1
        #「limit」を超える場合を確認し、「cnt」を初期化
        if cnt > limit:
            answer += power
        else:
            answer += cnt
        cnt = 0
    
    return answer